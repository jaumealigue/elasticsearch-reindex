# Elasticsearch-reindex

Elasticsearch-reindex is a set of scripts written in Python that allow to create backups of Elasticsearch indexes, as well as to recover those indexes.

- backup_elk.py --> It allows to reindex all the oldest indexes from X days ago, from an Elasticsearch to another Elasticsearch backup. 
- restore_elk.py --> It allows to recover an index from an Elasticsearch backup to another Elasticsearch.

## Installation
```bash
pip3 install elasticsearch
```
## Usage

#### backup_elk.py

```
$ python3 backup_elk.py

[+] Starting connection to Elasticsearch...

{'name': 'node-1', 'cluster_name': 'my-application', 'cluster_uuid': 'yltJ3XosRLO6Dzr_bafKXQ', 'version': {'number': '7.10.1', 'build_flavor': 'default', 'build_type': 'deb', 'build_hash': '1c34507e66d7db1211f66f3513706fdf548736aa', 'build_date': '2020-12-05T01:00:33.671820Z', 'build_snapshot': False, 'lucene_version': '8.7.0', 'minimum_wire_compatibility_version': '6.8.0', 'minimum_index_compatibility_version': '6.0.0-beta1'}, 'tagline': 'You Know, for Search'}
{'name': 'node-1', 'cluster_name': 'my-application', 'cluster_uuid': 'yltJ3XosRLO6Dzr_bafKXQ', 'version': {'number': '7.10.1', 'build_flavor': 'default', 'build_type': 'deb', 'build_hash': '1c34507e66d7db1211f66f3513706fdf548736aa', 'build_date': '2020-12-05T01:00:33.671820Z', 'build_snapshot': False, 'lucene_version': '8.7.0', 'minimum_wire_compatibility_version': '6.8.0', 'minimum_index_compatibility_version': '6.0.0-beta1'}, 'tagline': 'You Know, for Search'}

[+] Reindexing : filebeat-7.10.1-2021.01.06-000001
[+] Index reindexed : backup-filebeat-7.10.1-2021.01.06-000001
[+] Index closed : backup-filebeat-7.10.1-2021.01.06-000001

```

#### restore_elk.py
```
$ python3 restore_elk.py backup-filebeat-7.10.1-2021.01.06-000001

[+] Starting connection to Elasticsearch...

{'name': 'node-1', 'cluster_name': 'my-application', 'cluster_uuid': 'yltJ3XosRLO6Dzr_bafKXQ', 'version': {'number': '7.10.1', 'build_flavor': 'default', 'build_type': 'deb', 'build_hash': '1c34507e66d7db1211f66f3513706fdf548736aa', 'build_date': '2020-12-05T01:00:33.671820Z', 'build_snapshot': False, 'lucene_version': '8.7.0', 'minimum_wire_compatibility_version': '6.8.0', 'minimum_index_compatibility_version': '6.0.0-beta1'}, 'tagline': 'You Know, for Search'}
{'name': 'node-1', 'cluster_name': 'my-application', 'cluster_uuid': 'yltJ3XosRLO6Dzr_bafKXQ', 'version': {'number': '7.10.1', 'build_flavor': 'default', 'build_type': 'deb', 'build_hash': '1c34507e66d7db1211f66f3513706fdf548736aa', 'build_date': '2020-12-05T01:00:33.671820Z', 'build_snapshot': False, 'lucene_version': '8.7.0', 'minimum_wire_compatibility_version': '6.8.0', 'minimum_index_compatibility_version': '6.0.0-beta1'}, 'tagline': 'You Know, for Search'}

[+] Source index opened : backup-filebeat-7.10.1-2021.01.06-000001
[+] Reindexing : backup-filebeat-7.10.1-2021.01.06-000001
[+] Index reindexed : backup-filebeat-7.10.1-2021.01.06-000001
[+] Source index closed : backup-filebeat-7.10.1-2021.01.06-000001
```

## Contributing
Pull requests are welcome. 
Please make sure to update tests as appropriate.

