import json
import pickle
from IFETEL2019 import config
import numpy as np
pkl_file = config.EL_CANDIDATES_DATA_FILE
with open(pkl_file, 'rb') as f:
    (mstr_target_cnt_bisect_data, title_wid_bisect_data, redirects_bisect_data, entity_linked_cnts_dict) = pickle.load(f)

typed_mentions_file, sents_file=config.FIGER_FILES['typed-wiki-mentions'], config.WIKI_ANCHOR_SENTS_FILE

f_mention = open(typed_mentions_file, encoding='utf-8')
f_sent = open(sents_file, encoding='utf-8')
all_samples = list()
cur_sent = json.loads(next(f_sent))
mention_id = 0
for i, line in enumerate(f_mention):
    if (i + 1) % 1000000 == 0:
        print(i + 1)

f_mention.close()
f_sent.close()
