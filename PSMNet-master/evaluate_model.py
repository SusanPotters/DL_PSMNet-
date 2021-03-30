import matplotlib.pyplot as plt
import numpy as np

def read_file(path):
    with open(path, "r") as read_file:
        data = read_file.read()
        data = data.split(", ")
        del data[1::2]
        new = list(filter(None, data))

        for i, item in enumerate(new):
            if item == '0':
                new[i] = 0
            else:
                new[i] = float(item[7:-2])
        error_array = np.array(new)
    return error_array

def plot(error_array):
    plt.hist(error_array, color = 'blue', edgecolor = 'black', bins = 60)

    plt.title('Histogram of EPE Sceneflow')
    plt.xlabel('End-point-error')
    plt.ylabel('Samples')
    plt.tight_layout()
    plt.savefig('error_hist_sceneflow_monkaa.png')

def main():
    error_array = read_file("test_sceneflow_scenflow_trained.txt")
    plot(error_array)

if __name__ == '__main__':
    main()
