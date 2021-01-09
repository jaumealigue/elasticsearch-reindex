#!/usr/bin/env python3

import re
from datetime import datetime
from elasticsearch import Elasticsearch


####### Modify the following variables according to your scenario #########

# Source Elasticsearch
srcElastic = "http://192.168.1.118:9200"

# Destination Elasticsearch (backup)
dstElastic = "http://192.168.1.71:9200"

# Backup days. ex: 30 days --> All index created before 30 days ago.
daysBackup = 30

###########################################################################

print('\n[+] Starting connection to Elasticsearch...\n')

esDst = Elasticsearch(dstElastic)
esSrc = Elasticsearch(srcElastic)

print(esDst.info())
print(esSrc.info())

indices_state = esSrc.cluster.state()['metadata']['indices']

for source_index in sorted(indices_state.keys(), reverse=True):

    # In this case we are looking for all filebeat indexes.
    if re.match(r'^filebeat*', source_index):

        datelog = datetime.strptime(source_index.split("-")[2], '%Y.%m.%d')
        today = datetime.today()
        diff = today - datelog

        if diff.days >= daysBackup:

            destination_index = "backup-{0}".format(source_index)

            print("\n[+] Reindexing : " + source_index)

            result = esDst.reindex({
                "source": {"remote": {"host": srcElastic}, "index": source_index},
                "dest": {"index": destination_index}
            }, wait_for_completion=True, request_timeout=500000)

            # We check if during the reindex any error has occurred
            if result['timed_out'] == False and result['failures'] == []:

                print("[+] Index reindexed : " + destination_index)

                esDst.indices.close(destination_index)

                print("[+] Index closed : " + destination_index)

            else:

                print("[-] An ERROR occurred while reindexing... : ")
                print(result)








