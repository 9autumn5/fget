from NFETCCLSC2019.utils import logging_utils, data_utils, embedding_utils, pkl_utils
from NFETCCLSC2019 import config

words, mentions, positions, labels = data_utils.load(config.ONTONOTES_TEST_CLEAN)