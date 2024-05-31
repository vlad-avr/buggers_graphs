import matplotlib.pyplot as plt

filenames = ["48882_2442.txt", "4442_2222.txt", "4816842_248422.txt"]


class ParsedRun:
    def __init__(self, name, gen_stamps, time_stamps, fit_stamps, count_stamps) -> None:
        self.gen_stamps = gen_stamps
        self.name = name
        self.time_stamps = time_stamps
        self.fit_stamps = fit_stamps
        self.count_stamps = count_stamps
        
    def display(self):
        font_size = 6
        for i in range(1, len(self.gen_stamps)):
            plt.text(self.gen_stamps[i-1]*10, self.fit_stamps[i-1][0][0], self.fit_stamps[i-1][0][0], fontsize=font_size, ha='center', va='bottom')
            plt.text(self.gen_stamps[i-1]*10, self.fit_stamps[i-1][0][1], self.fit_stamps[i-1][0][1], fontsize=font_size, ha='center', va='bottom')
            plt.text(self.gen_stamps[i-1]*10, self.fit_stamps[i-1][0][2], self.fit_stamps[i-1][0][2], fontsize=font_size, ha='center', va='bottom')
            plt.text(self.gen_stamps[i-1]*10, self.fit_stamps[i-1][1][0], self.fit_stamps[i-1][1][0], fontsize=font_size, ha='center', va='bottom')
            plt.text(self.gen_stamps[i-1]*10, self.fit_stamps[i-1][1][1], self.fit_stamps[i-1][1][1], fontsize=font_size, ha='center', va='bottom')
            plt.text(self.gen_stamps[i-1]*10, self.fit_stamps[i-1][1][2], self.fit_stamps[i-1][1][2], fontsize=font_size, ha='center', va='bottom')
            plt.plot([self.gen_stamps[i-1]*10, self.gen_stamps[i]*10], [self.fit_stamps[i-1][0][0], self.fit_stamps[i][0][0]], c="#0000FF", ls=":")
            plt.plot([self.gen_stamps[i-1]*10, self.gen_stamps[i]*10], [self.fit_stamps[i-1][0][1], self.fit_stamps[i][0][1]], c="#00FFFF", ls="-")
            plt.plot([self.gen_stamps[i-1]*10, self.gen_stamps[i]*10], [self.fit_stamps[i-1][0][2], self.fit_stamps[i][0][2]], c="#00FF00", ls=":")
            plt.plot([self.gen_stamps[i-1]*10, self.gen_stamps[i]*10], [self.fit_stamps[i-1][1][0], self.fit_stamps[i][1][0]], c="#FFFF00", ls=":")
            plt.plot([self.gen_stamps[i-1]*10, self.gen_stamps[i]*10], [self.fit_stamps[i-1][1][1], self.fit_stamps[i][1][1]], c="#FF7300", ls="-")
            plt.plot([self.gen_stamps[i-1]*10, self.gen_stamps[i]*10], [self.fit_stamps[i-1][1][2], self.fit_stamps[i][1][2]], c="#FF0000", ls=":")
        plt.text(self.gen_stamps[len(self.gen_stamps)-1]*10, self.fit_stamps[len(self.gen_stamps)-1][0][0], self.fit_stamps[len(self.gen_stamps)-1][0][0], fontsize=font_size, ha='center', va='bottom')
        plt.text(self.gen_stamps[len(self.gen_stamps)-1]*10, self.fit_stamps[len(self.gen_stamps)-1][0][1], self.fit_stamps[len(self.gen_stamps)-1][0][1], fontsize=font_size, ha='center', va='bottom')
        plt.text(self.gen_stamps[len(self.gen_stamps)-1]*10, self.fit_stamps[len(self.gen_stamps)-1][0][2], self.fit_stamps[len(self.gen_stamps)-1][0][2], fontsize=font_size, ha='center', va='bottom')
        plt.text(self.gen_stamps[len(self.gen_stamps)-1]*10, self.fit_stamps[len(self.gen_stamps)-1][1][0], self.fit_stamps[len(self.gen_stamps)-1][1][0], fontsize=font_size, ha='center', va='bottom')
        plt.text(self.gen_stamps[len(self.gen_stamps)-1]*10, self.fit_stamps[len(self.gen_stamps)-1][1][1], self.fit_stamps[len(self.gen_stamps)-1][1][1], fontsize=font_size, ha='center', va='bottom')
        plt.text(self.gen_stamps[len(self.gen_stamps)-1]*10, self.fit_stamps[len(self.gen_stamps)-1][1][2], self.fit_stamps[len(self.gen_stamps)-1][1][2], fontsize=font_size, ha='center', va='bottom')
        plt.xlabel('Generations')
        plt.ylabel('Values')
        plt.title(self.name + " : NNet fitness Comparison")
        plt.grid(True)
        plt.show()
        for i in range(1, len(self.gen_stamps)):
            plt.text(self.gen_stamps[i-1]*10, self.count_stamps[i-1][0], str(self.count_stamps[i-1][0]), fontsize=font_size, ha='center', va='bottom')
            plt.plot([self.gen_stamps[i-1]*10, self.gen_stamps[i]*10], [self.count_stamps[i-1][0], self.count_stamps[i][0]], "b--")
            plt.text(self.gen_stamps[i-1]*10, self.count_stamps[i-1][1], str(self.count_stamps[i-1][1]), fontsize=font_size, ha='center', va='bottom')
            plt.plot([self.gen_stamps[i-1]*10, self.gen_stamps[i]*10], [self.count_stamps[i-1][1], self.count_stamps[i][1]], "r--")
            plt.text(self.gen_stamps[i-1]*10, self.time_stamps[i-1], str(self.time_stamps[i-1]), fontsize=font_size, ha='center', va='bottom')
            plt.plot([self.gen_stamps[i-1]*10, self.gen_stamps[i]*10], [self.time_stamps[i-1], self.time_stamps[i]], "y:")
        plt.text(self.gen_stamps[len(self.gen_stamps)-1]*10, self.time_stamps[len(self.gen_stamps)-1], str(self.time_stamps[len(self.gen_stamps)-1]), fontsize=font_size, ha='center', va='bottom')
        plt.text(self.gen_stamps[len(self.gen_stamps)-1]*10, self.count_stamps[len(self.gen_stamps)-1][0], str(self.count_stamps[len(self.gen_stamps)-1][0]), fontsize=font_size, ha='center', va='bottom')
        plt.text(self.gen_stamps[len(self.gen_stamps)-1]*10, self.count_stamps[len(self.gen_stamps)-1][1], str(self.count_stamps[len(self.gen_stamps)-1][1]), fontsize=font_size, ha='center', va='bottom')
        plt.xlabel('Generations')
        plt.ylabel('Values')
        plt.title(self.name + " : Count Comparison")
        plt.grid(True)
        plt.show()
            

def parse_file(file_name):
    lines = []
    with open(file_name, "r") as file:
        lines = file.readlines()
    runs = []
    gen_stamps = []
    time_stamps = []
    fit_stamps = []
    count_stamps = []
    name_id = 1
    i = 0
    while i < len(lines):
        gen_stamps.append(int(lines[i]))
        i+=1
        prey_num = int(lines[i])
        i+=1
        prey_fit_line = lines[i].split(" ")
        prey_fit = []
        for fit in prey_fit_line:
            prey_fit.append(float(fit))
        i+=1
        pred_num = int(lines[i])
        count_stamps.append([prey_num, pred_num])
        i+=1
        pred_fit_line = lines[i].split(" ")
        pred_fit = []
        for fit in pred_fit_line:
            pred_fit.append(float(fit))
        fit_stamps.append([prey_fit, pred_fit])
        i+=1
        time_stamps.append(int(lines[i]))
        i+=1
        if(i == name_id*30*6):
            runs.append(ParsedRun(name=f"Run {name_id}", gen_stamps=gen_stamps.copy(), time_stamps=time_stamps.copy(), fit_stamps=fit_stamps.copy(), count_stamps=count_stamps.copy()))
            name_id+=1
            gen_stamps.clear()
            time_stamps.clear()
            fit_stamps.clear()
            count_stamps.clear()
    return runs

def display_run_set(runs):
    for run in runs:
        run.display()

for n in filenames:
    display_run_set(parse_file(n))