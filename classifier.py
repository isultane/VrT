import fasttext
import os
import sys
import os.path
import numpy as np
from numpy import array
from sklearn.model_selection import KFold
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
import json
import traceback

# for imbalance data, we used oversamling to solve the minority classes problems 
from  imblearn.over_sampling import SMOTE, ADASYN

from preprocessing import extract_top_25_cwes

def predict_labels(testfile, model):
    # Return predictions
    lines = open(testfile, 'r').readlines()
    pred_label = []
   
    for line in lines:
        text = ' '.join(line.split()[2:])
        label = model.predict(text)[0][0]
        pred_label.append(label)
        
    return pred_label

def parse_labels(testfile):
    #return test labeles
    lines = open(testfile, 'r').readlines()
    test_lables = []
    sec = 1
    nonsec = 0
    count = 0
    for line in lines:
        #count +=1
        label = line.split()[0]
        test_lables.append(label)
    #print(count + 'lables has been read')
    return test_lables

if __name__ == '__main__':
    extract_top_25_cwes()
    # data_set = './test/'

    # for file in os.listdir(data_set):
    #     print('Processing ' + file)

    #     f_out = './out_'+file
        
    #     path_train = './tmp/tmp_train.txt'
    #     path_test = './tmp/tmp_test.txt'

    #     model_fn = './vrt_model.bin'
    #     try:
    #         print("Converting dataset to array")
    #         f = open(data_set+file, 'r+', encoding="UTF-8")
    #         data = array(f.readlines())
    #         f.close()

    #         # array for details
    #         fold_outputs = []

    #         # 10 fold loop
    #         kfold = KFold(10, shuffle=True, random_state=1)
    #         fold = 1
    #         # the following portion of this code is modified verion from this reference:
    #         # https://github.com/ChristianBirchler/ticket-tagger-analysis/blob/main/code-pipeline/classifiers/classifier.py
    #         for train, test in kfold.split(data):
    #             print("New tenfold iteration:", str(fold), "-----------------------------------------")
    #             print("Creating train file")
    #             tmp_train = open(path_train, "w", encoding="UTF-8")
    #             for line in data[train]:
    #                 tmp_train.write("".join(line))
    #             tmp_train.close()

    #             print("Creating test file")
    #             tmp_test = open(path_test, "w", encoding="UTF-8")
    #             for line in data[test]:
    #                 tmp_test.write("".join(line))
    #             tmp_test.close()

            
    #             print("start training...")
            
    #             fasttext_params = {
    #                 'input': path_train,
    #                 'lr': 0.90,
    #                 'lrUpdateRate': 1000,
    #                 'epoch': 25,
    #                 'wordNgrams': 2,
    #                 'loss': 'ova'
    #             }
    #             model = fasttext.train_supervised(**fasttext_params)  
            
    #             print("start testing...")
    #             y_true = parse_labels(path_test)
    #             y_pred = predict_labels(path_test, model)
            

    #             # Print the precision and recall, among other metrics
    #             report = metrics.classification_report(y_true, y_pred, digits=3, zero_division=1, output_dict=True)       
            
    #             precision = report['weighted avg']['precision']
    #             recall = report['weighted avg']['recall'] 
    #             f_score = report['weighted avg']['f1-score']

    #             result = {
    #                 '10-Fold iteration:': fold,
    #                 'F1': f_score,
    #                 'Recall': recall,
    #                 'Precision': precision
    #             }
    #             # log
    #             print("Fold over, here are results: ")
    #             print(json.dumps(result, indent=4))
    #             fold_outputs.append(result)
    #             fold += 1

    #             # save best fold_model.bin for testing
    #             if f_score >= result["F1"]:
    #                 if os.path.exists(model_fn):
    #                     os.remove(model_fn)
    #                 model.save_model(model_fn)
    #         print("Done with 10 fold validation")
    #         # calculate over-all results
    #         mean_recall = 0
    #         mean_precision = 0
    #         mean_f1 = 0
    #         for f in fold_outputs:
    #             mean_f1 += (f['F1'] / 10)
    #             mean_recall += (f['Recall'] / 10)
    #             mean_precision += (f['Precision'] / 10)
    #             # compile results as json
    #         output = {
    #             'Results': {
    #                 'F1': mean_f1,
    #                 'Recall': mean_recall,
    #                 'Precision': mean_precision
    #             },
    #             'Details': fold_outputs
    #         }
    #         dump = json.dumps(output, indent=4)
    #         print(dump)
    #         # write to output
    #         print("Writing output to file")
    #         o = open(f_out, 'w', encoding="UTF-8")
    #         o.write(dump)
    #         o.close()

    #     except Exception as e:
    #         print("An Error occurred")
    #         print(str(e))
    #         traceback.print_exc()
    #     # in any case delete existing temporary files
    #     finally:
    #         print("Deleting tmp files")
    #         if os.path.exists(path_train):
    #             os.remove(path_train)
    #         if os.path.exists(path_test):
    #             os.remove(path_test)
    #         print("Exit.")
