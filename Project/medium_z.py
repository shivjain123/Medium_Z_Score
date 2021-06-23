import csv
import pandas as p
import plotly.figure_factory as pff
import plotly.graph_objects as go
import random as r
import statistics as s

df = p.read_csv("D:/(4) WhiteHatJr. Codes/Third Module/z-test/Project/csv files/School2.csv")

math_score = df["Math_score"].tolist()

population_mean = s.mean(math_score)
population_sd = s.stdev(math_score)

figure = pff.create_distplot([math_score], ["Results"], show_hist = False)

#figure.show()

print()
print("The Population Mean is {m}".format(m=population_mean))
print()
print("The Population Standard Deviation is {sd}".format(sd=population_sd))
print()

def random_set_of_means(counter):
    random_list = list()
    for i in range(100):
        random_index = r.randint(0, len(math_score) - 1)
        random_list.append(math_score[random_index])
    mean_of_random = s.mean(random_list)
    return mean_of_random


def setup():
    list_of_means = list()
    for i in range(100):
        set_of_means = random_set_of_means(30)
        list_of_means.append(set_of_means)
    main_mean = s.mean(list_of_means)

    print("The Sampling Mean is {m}".format(m=main_mean))
    print()
    print("The Sampling Standard Deviation is {sd}".format(sd=s.stdev(list_of_means)))
    print()

    #Sample Mean for first intervention
    i1 = p.read_csv("D:/(4) WhiteHatJr. Codes/Third Module/z-test/Project/csv files/School_1_Sample.csv")
    math_score_i1 = i1["Math_score"].tolist()
    mean_i1 = s.mean(math_score_i1)

    print("The Mean of the First Intervention is {m}.".format(m=mean_i1))
    print()

    #Sample Mean for second intervention
    i2 = p.read_csv("D:/(4) WhiteHatJr. Codes/Third Module/z-test/Project/csv files/School_2_Sample.csv")
    math_score_i2 = i2["Math_score"].tolist()
    mean_i2 = s.mean(math_score_i2)

    print("The Mean of the Second Intervention is {m}.".format(m=mean_i2))
    print()

    #Sample Mean for third intervention
    i3 = p.read_csv("D:/(4) WhiteHatJr. Codes/Third Module/z-test/Project/csv files/School_3_Sample.csv")
    math_score_i3 = i3["Math_score"].tolist()
    mean_i3 = s.mean(math_score_i3)

    print("The Mean of the Third Intervention is {m}.".format(m=mean_i3))
    print()

    first_sd_left, first_sd_right = population_mean-population_sd, population_mean+population_sd
    second_sd_left, second_sd_right = population_mean-population_sd*2, population_mean+population_sd*2
    third_sd_left, third_sd_right = population_mean-population_sd*3, population_mean+population_sd*3

    figure_new = pff.create_distplot([list_of_means], ["Results"], show_hist=False)

    figure_new.add_trace(go.Scatter(x=[main_mean, main_mean], y=[0, 0.14], mode="lines", name="Mean"))

    figure_new.add_trace(go.Scatter(x=[first_sd_left, first_sd_left], y=[0, 0.14], mode="lines", name="First SD Left"))
    figure_new.add_trace(go.Scatter(x=[first_sd_right, first_sd_right], y=[0, 0.14], mode="lines", name="First SD Right"))

    figure_new.add_trace(go.Scatter(x=[second_sd_left, second_sd_left], y=[0, 0.14], mode="lines", name="Second SD Left"))
    figure_new.add_trace(go.Scatter(x=[second_sd_right, second_sd_right], y=[0, 0.14], mode="lines", name="Second SD Right"))

    figure_new.add_trace(go.Scatter(x=[third_sd_left, third_sd_left], y=[0, 0.14], mode="lines", name="Third SD Left"))
    figure_new.add_trace(go.Scatter(x=[third_sd_right, third_sd_right], y=[0, 0.14], mode="lines", name="Third SD Right"))

    figure_new.add_trace(go.Scatter(x = [mean_i1, mean_i1], y = [0, 0.14], mode = "lines", name = "Mean of First Intervention"))
    figure_new.add_trace(go.Scatter(x = [mean_i2, mean_i2], y = [0, 0.14], mode = "lines", name = "Mean of Second Intervention"))
    figure_new.add_trace(go.Scatter(x = [mean_i3, mean_i3], y = [0, 0.14], mode="lines", name = "Mean of Thrid Intervention"))

    figure_new.show()

    # Z-Score for First Intervention
    print("The Z Score for First Intevention is {z}".format(z = ((main_mean - mean_i1)/population_sd)))
    print()
    # Z-Score for Second Intervention
    print("The Z Score for Second Intevention is {z}".format(z = ((main_mean - mean_i2)/population_sd)))
    print()
    # Z-Score for Third Intervention
    print("The Z Score for Third Intevention is {z}".format(z = ((main_mean - mean_i3)/population_sd)))
    print()

if __name__ == '__main__':
    setup()