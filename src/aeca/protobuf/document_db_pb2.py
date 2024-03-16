# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: document_db.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import aeca.protobuf.document_pb2 as document__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x64ocument_db.proto\x12\x17\x63ognica.rpc.db.document\x1a\x0e\x64ocument.proto\"\xf9\x01\n\x0fIndexDescriptor\x12\x10\n\x08index_id\x18\x01 \x01(\r\x12\x12\n\nindex_name\x18\x02 \x01(\t\x12\x0e\n\x06\x66ields\x18\x03 \x03(\t\x12\x0e\n\x06unique\x18\x04 \x01(\x08\x12\x36\n\nindex_type\x18\x05 \x01(\x0e\x32\".cognica.rpc.db.document.IndexType\x12\x34\n\x06status\x18\x06 \x01(\x0e\x32$.cognica.rpc.db.document.IndexStatus\x12\x32\n\x07options\x18\x07 \x01(\x0b\x32!.cognica.rpc.db.document.Document\"\xa6\x01\n\rFTSFieldStats\x12\x12\n\nfield_name\x18\x01 \x01(\t\x12\x17\n\x0ftotal_doc_count\x18\x02 \x01(\x03\x12\x16\n\x0etotal_doc_size\x18\x03 \x01(\x03\x12\x11\n\tdoc_count\x18\x04 \x01(\x03\x12\x10\n\x08\x64oc_size\x18\x05 \x01(\x03\x12\x15\n\rsum_term_freq\x18\x06 \x01(\x03\x12\x14\n\x0csum_doc_freq\x18\x07 \x01(\x03\"q\n\rFTSIndexStats\x12\x11\n\tdoc_count\x18\x01 \x01(\x03\x12\x10\n\x08\x64oc_size\x18\x02 \x01(\x03\x12;\n\x0b\x66ield_stats\x18\x03 \x03(\x0b\x32&.cognica.rpc.db.document.FTSFieldStats\"\xcf\x02\n\nIndexStats\x12\x10\n\x08index_id\x18\x01 \x01(\r\x12\x12\n\nindex_name\x18\x02 \x01(\t\x12\x19\n\x11\x61pproximated_size\x18\x03 \x01(\x04\x12\x10\n\x08num_docs\x18\x04 \x01(\x04\x12\x10\n\x08\x61\x63\x63\x65ssed\x18\x05 \x01(\x04\x12\r\n\x05\x61\x64\x64\x65\x64\x18\x06 \x01(\x04\x12\x0f\n\x07updated\x18\x07 \x01(\x04\x12\x0f\n\x07\x64\x65leted\x18\x08 \x01(\x04\x12\x0e\n\x06merged\x18\t \x01(\x04\x12\x13\n\x0b\x61\x63\x63\x65ssed_at\x18\n \x01(\x03\x12\x10\n\x08\x61\x64\x64\x65\x64_at\x18\x0b \x01(\x03\x12\x12\n\nupdated_at\x18\x0c \x01(\x03\x12\x12\n\ndeleted_at\x18\r \x01(\x03\x12\x11\n\tmerged_at\x18\x0e \x01(\x03\x12\x39\n\tfts_stats\x18\x0f \x01(\x0b\x32&.cognica.rpc.db.document.FTSIndexStats\"\xa8\x01\n\x0e\x43ollectionInfo\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x43\n\x11index_descriptors\x18\x02 \x03(\x0b\x32(.cognica.rpc.db.document.IndexDescriptor\x12\x38\n\x0bindex_stats\x18\x03 \x03(\x0b\x32#.cognica.rpc.db.document.IndexStats\"\x7f\n\x0bProfileInfo\x12\x0f\n\x07matched\x18\x01 \x01(\x04\x12\x0f\n\x07scanned\x18\x02 \x01(\x04\x12\x10\n\x08\x66iltered\x18\x03 \x01(\x04\x12\x19\n\x11query_duration_us\x18\x04 \x01(\x04\x12!\n\x19serialization_duration_us\x18\x05 \x01(\x04\"V\n\x17\x43reateCollectionRequest\x12;\n\ncollection\x18\x01 \x01(\x0b\x32\'.cognica.rpc.db.document.CollectionInfo\"r\n\x18\x43reateCollectionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x35\n\x07profile\x18\x03 \x01(\x0b\x32$.cognica.rpc.db.document.ProfileInfo\"0\n\x15\x44ropCollectionRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\"p\n\x16\x44ropCollectionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x35\n\x07profile\x18\x03 \x01(\x0b\x32$.cognica.rpc.db.document.ProfileInfo\"S\n\x17RenameCollectionRequest\x12\x1b\n\x13old_collection_name\x18\x01 \x01(\t\x12\x1b\n\x13new_collection_name\x18\x02 \x01(\t\"r\n\x18RenameCollectionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x35\n\x07profile\x18\x03 \x01(\x0b\x32$.cognica.rpc.db.document.ProfileInfo\"/\n\x14GetCollectionRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\"\xac\x01\n\x15GetCollectionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12;\n\ncollection\x18\x03 \x01(\x0b\x32\'.cognica.rpc.db.document.CollectionInfo\x12\x35\n\x07profile\x18\x04 \x01(\x0b\x32$.cognica.rpc.db.document.ProfileInfo\"1\n\x15GetCollectionsRequest\x12\x18\n\x10\x63ollection_names\x18\x01 \x03(\t\"\xae\x01\n\x16GetCollectionsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12<\n\x0b\x63ollections\x18\x03 \x03(\x0b\x32\'.cognica.rpc.db.document.CollectionInfo\x12\x35\n\x07profile\x18\x04 \x01(\x0b\x32$.cognica.rpc.db.document.ProfileInfo\"k\n\x12\x43reateIndexRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12<\n\nindex_desc\x18\x02 \x01(\x0b\x32(.cognica.rpc.db.document.IndexDescriptor\"m\n\x13\x43reateIndexResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x35\n\x07profile\x18\x03 \x01(\x0b\x32$.cognica.rpc.db.document.ProfileInfo\"?\n\x10\x44ropIndexRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x12\n\nindex_name\x18\x02 \x01(\t\"k\n\x11\x44ropIndexResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x35\n\x07profile\x18\x03 \x01(\x0b\x32$.cognica.rpc.db.document.ProfileInfo\"]\n\x12RenameIndexRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x16\n\x0eold_index_name\x18\x02 \x01(\t\x12\x16\n\x0enew_index_name\x18\x03 \x01(\t\"m\n\x13RenameIndexResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x35\n\x07profile\x18\x03 \x01(\x0b\x32$.cognica.rpc.db.document.ProfileInfo\">\n\x0fGetIndexRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x12\n\nindex_name\x18\x02 \x01(\t\"\xfb\x01\n\x10GetIndexResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x17\n\x0f\x63ollection_name\x18\x03 \x01(\t\x12<\n\nindex_desc\x18\x04 \x01(\x0b\x32(.cognica.rpc.db.document.IndexDescriptor\x12\x38\n\x0bindex_stats\x18\x05 \x01(\x0b\x32#.cognica.rpc.db.document.IndexStats\x12\x35\n\x07profile\x18\x06 \x01(\x0b\x32$.cognica.rpc.db.document.ProfileInfo\"R\n\x05Query\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x30\n\x05query\x18\x02 \x01(\x0b\x32!.cognica.rpc.db.document.Document\"\xe4\x01\n\x0b\x46indRequest\x12-\n\x05query\x18\x01 \x01(\x0b\x32\x1e.cognica.rpc.db.document.Query\x12\r\n\x05limit\x18\x02 \x01(\x05\x12\x15\n\rindex_columns\x18\x03 \x03(\t\x12\x0f\n\x07\x63olumns\x18\x04 \x03(\t\x12@\n\x06\x64types\x18\x05 \x03(\x0b\x32\x30.cognica.rpc.db.document.FindRequest.DtypesEntry\x1a-\n\x0b\x44typesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"|\n\x0c\x46indResponse\x12\x13\n\x0bnum_columns\x18\x01 \x01(\x05\x12\x10\n\x08num_rows\x18\x02 \x01(\x05\x12\x0e\n\x06\x62uffer\x18\x03 \x01(\x0c\x12\x35\n\x07profile\x18\x04 \x01(\x0b\x32$.cognica.rpc.db.document.ProfileInfo\"J\n\x10\x46indBatchRequest\x12\x36\n\x08requests\x18\x01 \x03(\x0b\x32$.cognica.rpc.db.document.FindRequest\"M\n\x11\x46indBatchResponse\x12\x38\n\tresponses\x18\x01 \x03(\x0b\x32%.cognica.rpc.db.document.FindResponse\"=\n\x0c\x43ountRequest\x12-\n\x05query\x18\x01 \x01(\x0b\x32\x1e.cognica.rpc.db.document.Query\"v\n\rCountResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\r\n\x05\x63ount\x18\x03 \x01(\x03\x12\x35\n\x07profile\x18\x04 \x01(\x0b\x32$.cognica.rpc.db.document.ProfileInfo\"@\n\x0f\x43ontainsRequest\x12-\n\x05query\x18\x01 \x01(\x0b\x32\x1e.cognica.rpc.db.document.Query\"y\n\x10\x43ontainsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\r\n\x05\x66ound\x18\x03 \x01(\x08\x12\x35\n\x07profile\x18\x04 \x01(\x0b\x32$.cognica.rpc.db.document.ProfileInfo\"A\n\rInsertRequest\x12\x30\n\x08requests\x18\x01 \x03(\x0b\x32\x1e.cognica.rpc.db.document.Query\"h\n\x0eInsertResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x35\n\x07profile\x18\x03 \x01(\x0b\x32$.cognica.rpc.db.document.ProfileInfo\"\x8f\x01\n\rUpdateRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x31\n\x06\x66ilter\x18\x02 \x01(\x0b\x32!.cognica.rpc.db.document.Document\x12\x32\n\x07updates\x18\x03 \x01(\x0b\x32!.cognica.rpc.db.document.Document\"h\n\x0eUpdateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x35\n\x07profile\x18\x03 \x01(\x0b\x32$.cognica.rpc.db.document.ProfileInfo\"A\n\rRemoveRequest\x12\x30\n\x08requests\x18\x01 \x03(\x0b\x32\x1e.cognica.rpc.db.document.Query\"h\n\x0eRemoveResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x35\n\x07profile\x18\x03 \x01(\x0b\x32$.cognica.rpc.db.document.ProfileInfo\"A\n\x0e\x45xplainRequest\x12/\n\x07queries\x18\x01 \x03(\x0b\x32\x1e.cognica.rpc.db.document.Query\"m\n\tQueryPlan\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x17\n\x0f\x63ollection_name\x18\x03 \x01(\t\x12\x12\n\nindex_name\x18\x04 \x01(\t\x12\x12\n\nquery_plan\x18\x05 \x01(\t\"Z\n\x0f\x45xplainResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x37\n\x0bquery_plans\x18\x02 \x03(\x0b\x32\".cognica.rpc.db.document.QueryPlan\"4\n\x19TruncateCollectionRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\"t\n\x1aTruncateCollectionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x35\n\x07profile\x18\x03 \x01(\x0b\x32$.cognica.rpc.db.document.ProfileInfo\"\x18\n\x16ListCollectionsRequest\"\x8b\x01\n\x17ListCollectionsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x18\n\x10\x63ollection_names\x18\x03 \x03(\t\x12\x35\n\x07profile\x18\x04 \x01(\x0b\x32$.cognica.rpc.db.document.ProfileInfo*e\n\tIndexType\x12\x0f\n\x0bkPrimaryKey\x10\x00\x12\x11\n\rkSecondaryKey\x10\x01\x12\x1a\n\x16kClusteredSecondaryKey\x10\x02\x12\x18\n\x14kFullTextSearchIndex\x10\x03*\x8d\x01\n\x0bIndexStatus\x12\x0c\n\x08kEnabled\x10\x00\x12\r\n\tkDisabled\x10\x01\x12\x0f\n\x0bkReadyToUse\x10\x02\x12\x14\n\x10kBuildInProgress\x10\x03\x12\x12\n\x0ekBuildFinished\x10\x04\x12\x13\n\x0fkDropInProgress\x10\x05\x12\x11\n\rkDropFinished\x10\x06\x32\xfd\x0f\n\x11\x44ocumentDBService\x12U\n\x04\x66ind\x12$.cognica.rpc.db.document.FindRequest\x1a%.cognica.rpc.db.document.FindResponse\"\x00\x12\x65\n\nfind_batch\x12).cognica.rpc.db.document.FindBatchRequest\x1a*.cognica.rpc.db.document.FindBatchResponse\"\x00\x12X\n\x05\x63ount\x12%.cognica.rpc.db.document.CountRequest\x1a&.cognica.rpc.db.document.CountResponse\"\x00\x12\x61\n\x08\x63ontains\x12(.cognica.rpc.db.document.ContainsRequest\x1a).cognica.rpc.db.document.ContainsResponse\"\x00\x12[\n\x06insert\x12&.cognica.rpc.db.document.InsertRequest\x1a\'.cognica.rpc.db.document.InsertResponse\"\x00\x12[\n\x06update\x12&.cognica.rpc.db.document.UpdateRequest\x1a\'.cognica.rpc.db.document.UpdateResponse\"\x00\x12[\n\x06remove\x12&.cognica.rpc.db.document.RemoveRequest\x1a\'.cognica.rpc.db.document.RemoveResponse\"\x00\x12^\n\x07\x65xplain\x12\'.cognica.rpc.db.document.ExplainRequest\x1a(.cognica.rpc.db.document.ExplainResponse\"\x00\x12z\n\x11\x63reate_collection\x12\x30.cognica.rpc.db.document.CreateCollectionRequest\x1a\x31.cognica.rpc.db.document.CreateCollectionResponse\"\x00\x12t\n\x0f\x64rop_collection\x12..cognica.rpc.db.document.DropCollectionRequest\x1a/.cognica.rpc.db.document.DropCollectionResponse\"\x00\x12z\n\x11rename_collection\x12\x30.cognica.rpc.db.document.RenameCollectionRequest\x1a\x31.cognica.rpc.db.document.RenameCollectionResponse\"\x00\x12q\n\x0eget_collection\x12-.cognica.rpc.db.document.GetCollectionRequest\x1a..cognica.rpc.db.document.GetCollectionResponse\"\x00\x12t\n\x0fget_collections\x12..cognica.rpc.db.document.GetCollectionsRequest\x1a/.cognica.rpc.db.document.GetCollectionsResponse\"\x00\x12w\n\x10list_collections\x12/.cognica.rpc.db.document.ListCollectionsRequest\x1a\x30.cognica.rpc.db.document.ListCollectionsResponse\"\x00\x12\x80\x01\n\x13truncate_collection\x12\x32.cognica.rpc.db.document.TruncateCollectionRequest\x1a\x33.cognica.rpc.db.document.TruncateCollectionResponse\"\x00\x12k\n\x0c\x63reate_index\x12+.cognica.rpc.db.document.CreateIndexRequest\x1a,.cognica.rpc.db.document.CreateIndexResponse\"\x00\x12\x65\n\ndrop_index\x12).cognica.rpc.db.document.DropIndexRequest\x1a*.cognica.rpc.db.document.DropIndexResponse\"\x00\x12k\n\x0crename_index\x12+.cognica.rpc.db.document.RenameIndexRequest\x1a,.cognica.rpc.db.document.RenameIndexResponse\"\x00\x12\x62\n\tget_index\x12(.cognica.rpc.db.document.GetIndexRequest\x1a).cognica.rpc.db.document.GetIndexResponse\"\x00\x42\x03\xf8\x01\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'document_db_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\370\001\001'
  _globals['_FINDREQUEST_DTYPESENTRY']._options = None
  _globals['_FINDREQUEST_DTYPESENTRY']._serialized_options = b'8\001'
  _globals['_INDEXTYPE']._serialized_start=5351
  _globals['_INDEXTYPE']._serialized_end=5452
  _globals['_INDEXSTATUS']._serialized_start=5455
  _globals['_INDEXSTATUS']._serialized_end=5596
  _globals['_INDEXDESCRIPTOR']._serialized_start=63
  _globals['_INDEXDESCRIPTOR']._serialized_end=312
  _globals['_FTSFIELDSTATS']._serialized_start=315
  _globals['_FTSFIELDSTATS']._serialized_end=481
  _globals['_FTSINDEXSTATS']._serialized_start=483
  _globals['_FTSINDEXSTATS']._serialized_end=596
  _globals['_INDEXSTATS']._serialized_start=599
  _globals['_INDEXSTATS']._serialized_end=934
  _globals['_COLLECTIONINFO']._serialized_start=937
  _globals['_COLLECTIONINFO']._serialized_end=1105
  _globals['_PROFILEINFO']._serialized_start=1107
  _globals['_PROFILEINFO']._serialized_end=1234
  _globals['_CREATECOLLECTIONREQUEST']._serialized_start=1236
  _globals['_CREATECOLLECTIONREQUEST']._serialized_end=1322
  _globals['_CREATECOLLECTIONRESPONSE']._serialized_start=1324
  _globals['_CREATECOLLECTIONRESPONSE']._serialized_end=1438
  _globals['_DROPCOLLECTIONREQUEST']._serialized_start=1440
  _globals['_DROPCOLLECTIONREQUEST']._serialized_end=1488
  _globals['_DROPCOLLECTIONRESPONSE']._serialized_start=1490
  _globals['_DROPCOLLECTIONRESPONSE']._serialized_end=1602
  _globals['_RENAMECOLLECTIONREQUEST']._serialized_start=1604
  _globals['_RENAMECOLLECTIONREQUEST']._serialized_end=1687
  _globals['_RENAMECOLLECTIONRESPONSE']._serialized_start=1689
  _globals['_RENAMECOLLECTIONRESPONSE']._serialized_end=1803
  _globals['_GETCOLLECTIONREQUEST']._serialized_start=1805
  _globals['_GETCOLLECTIONREQUEST']._serialized_end=1852
  _globals['_GETCOLLECTIONRESPONSE']._serialized_start=1855
  _globals['_GETCOLLECTIONRESPONSE']._serialized_end=2027
  _globals['_GETCOLLECTIONSREQUEST']._serialized_start=2029
  _globals['_GETCOLLECTIONSREQUEST']._serialized_end=2078
  _globals['_GETCOLLECTIONSRESPONSE']._serialized_start=2081
  _globals['_GETCOLLECTIONSRESPONSE']._serialized_end=2255
  _globals['_CREATEINDEXREQUEST']._serialized_start=2257
  _globals['_CREATEINDEXREQUEST']._serialized_end=2364
  _globals['_CREATEINDEXRESPONSE']._serialized_start=2366
  _globals['_CREATEINDEXRESPONSE']._serialized_end=2475
  _globals['_DROPINDEXREQUEST']._serialized_start=2477
  _globals['_DROPINDEXREQUEST']._serialized_end=2540
  _globals['_DROPINDEXRESPONSE']._serialized_start=2542
  _globals['_DROPINDEXRESPONSE']._serialized_end=2649
  _globals['_RENAMEINDEXREQUEST']._serialized_start=2651
  _globals['_RENAMEINDEXREQUEST']._serialized_end=2744
  _globals['_RENAMEINDEXRESPONSE']._serialized_start=2746
  _globals['_RENAMEINDEXRESPONSE']._serialized_end=2855
  _globals['_GETINDEXREQUEST']._serialized_start=2857
  _globals['_GETINDEXREQUEST']._serialized_end=2919
  _globals['_GETINDEXRESPONSE']._serialized_start=2922
  _globals['_GETINDEXRESPONSE']._serialized_end=3173
  _globals['_QUERY']._serialized_start=3175
  _globals['_QUERY']._serialized_end=3257
  _globals['_FINDREQUEST']._serialized_start=3260
  _globals['_FINDREQUEST']._serialized_end=3488
  _globals['_FINDREQUEST_DTYPESENTRY']._serialized_start=3443
  _globals['_FINDREQUEST_DTYPESENTRY']._serialized_end=3488
  _globals['_FINDRESPONSE']._serialized_start=3490
  _globals['_FINDRESPONSE']._serialized_end=3614
  _globals['_FINDBATCHREQUEST']._serialized_start=3616
  _globals['_FINDBATCHREQUEST']._serialized_end=3690
  _globals['_FINDBATCHRESPONSE']._serialized_start=3692
  _globals['_FINDBATCHRESPONSE']._serialized_end=3769
  _globals['_COUNTREQUEST']._serialized_start=3771
  _globals['_COUNTREQUEST']._serialized_end=3832
  _globals['_COUNTRESPONSE']._serialized_start=3834
  _globals['_COUNTRESPONSE']._serialized_end=3952
  _globals['_CONTAINSREQUEST']._serialized_start=3954
  _globals['_CONTAINSREQUEST']._serialized_end=4018
  _globals['_CONTAINSRESPONSE']._serialized_start=4020
  _globals['_CONTAINSRESPONSE']._serialized_end=4141
  _globals['_INSERTREQUEST']._serialized_start=4143
  _globals['_INSERTREQUEST']._serialized_end=4208
  _globals['_INSERTRESPONSE']._serialized_start=4210
  _globals['_INSERTRESPONSE']._serialized_end=4314
  _globals['_UPDATEREQUEST']._serialized_start=4317
  _globals['_UPDATEREQUEST']._serialized_end=4460
  _globals['_UPDATERESPONSE']._serialized_start=4462
  _globals['_UPDATERESPONSE']._serialized_end=4566
  _globals['_REMOVEREQUEST']._serialized_start=4568
  _globals['_REMOVEREQUEST']._serialized_end=4633
  _globals['_REMOVERESPONSE']._serialized_start=4635
  _globals['_REMOVERESPONSE']._serialized_end=4739
  _globals['_EXPLAINREQUEST']._serialized_start=4741
  _globals['_EXPLAINREQUEST']._serialized_end=4806
  _globals['_QUERYPLAN']._serialized_start=4808
  _globals['_QUERYPLAN']._serialized_end=4917
  _globals['_EXPLAINRESPONSE']._serialized_start=4919
  _globals['_EXPLAINRESPONSE']._serialized_end=5009
  _globals['_TRUNCATECOLLECTIONREQUEST']._serialized_start=5011
  _globals['_TRUNCATECOLLECTIONREQUEST']._serialized_end=5063
  _globals['_TRUNCATECOLLECTIONRESPONSE']._serialized_start=5065
  _globals['_TRUNCATECOLLECTIONRESPONSE']._serialized_end=5181
  _globals['_LISTCOLLECTIONSREQUEST']._serialized_start=5183
  _globals['_LISTCOLLECTIONSREQUEST']._serialized_end=5207
  _globals['_LISTCOLLECTIONSRESPONSE']._serialized_start=5210
  _globals['_LISTCOLLECTIONSRESPONSE']._serialized_end=5349
  _globals['_DOCUMENTDBSERVICE']._serialized_start=5599
  _globals['_DOCUMENTDBSERVICE']._serialized_end=7644
# @@protoc_insertion_point(module_scope)