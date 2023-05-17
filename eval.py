import numpy
import pandas
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score


def calc_metrics(path_result_file):
    results = numpy.array(pandas.read_excel(path_result_file, header=None))

    k = 5
    idx = numpy.array_split(numpy.arange(results.shape[0]), k)
    r2_scores = list()
    maes = list()

    for k in range(0, k):
        r2_scores.append(r2_score(results[idx[k], 1], results[idx[k], 2]))
        maes.append(mean_absolute_error(results[idx[k], 1], results[idx[k], 2]))

    print(numpy.round(numpy.mean(r2_scores), 3), numpy.round(numpy.std(r2_scores), 3))
    print(numpy.round(numpy.mean(maes), 3), numpy.round(numpy.std(maes), 3))
    print('------------------------')


calc_metrics('save/preds_lipo.xlsx')
# calc_metrics('save/preds_esol.xlsx')
# calc_metrics('save/preds_admet_logs.xlsx')
# calc_metrics('save/preds_igc50.xlsx')
# calc_metrics('save/preds_lc50.xlsx')
# calc_metrics('save/preds_ld50.xlsx')
# calc_metrics('save/preds_lmc-h.xlsx')
calc_metrics('save/preds_lmc-r.xlsx')
