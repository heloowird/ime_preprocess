# step1
#python process_pinyin.py ../data/chinese_chatbot_corpus/clean_chat_corpus ../output/corpus

# step2
#rm -rf ../output/dict
#mkdir -p ../output/dict
#python gen_token_dict.py ../output/corpus ../output/dict

# step3
#python merge_token_dict.py ../output/dict

# step4
#rm -rf ../output/sample
#mkdir -p ../output/sample
#python make_char2hanzi_seq_sample.py ../output/corpus ../output/dict/hz_dict_tot.txt ../output/dict/py_dict_tot.txt ../output/sample


