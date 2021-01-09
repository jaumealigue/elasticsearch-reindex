# !/usr/bin/env python3

import sys
from elasticsearch import Elasticsearch


if len(sys.argv)==1:
    print("\n[-] ERROR: Please enter an index as argument")
    exit()

index = str(sys.argv[1])

####### Modify the following variables according to your scenario #########

# Source Elasticsearch (backup)
srcElastic = "http://192.168.1.71:9200"

# Destination Elasticsearch
dstElastic = "http://192.168.1.118:9200"

###########################################################################

print('\n[+] Starting connection to Elasticsearch...\n')

esDst = Elasticsearch(dstElastic)
esSrc = Elasticsearch(srcElastic)

print(esDst.info())
print(esSrc.info())

indices_state = esSrc.cluster.state()['metadata']['indices']

for source_index in sorted(indices_state.keys(), reverse=True):

    if index == source_index:

        esSrc.indices.open(index)

        print("\n[+] Source index opened : " + source_index)

        print("[+] Reindexing : " + source_index)

        result = esDst.reindex({
            "source": {"remote": {"host": srcElastic}, "index": source_index},
            "dest": {"index": source_index}
        }, wait_for_completion=True, request_timeout=500000)

        # We check if during the reindex any error has occurred
        if result['timed_out'] == False and result['failures'] == []:

            print("[+] Index reindexed : " + source_index)

            esSrc.indices.close(source_index)

            print("[+] Source index closed : " + source_index)

        else:

            esSrc.indices.close(source_index)

            print("[-] An ERROR occurred while reindexing... : ")
            print(result)