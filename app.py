import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

font_path = './font/NotoSansKR-Bold.ttf'
fontprop = fm.FontProperties(fname=font_path)

# plt.rcParams['font.family'] = fontprop.get_name()
# plt.rcParams['axes.unicode_minus'] = False

years = [1970, 1980, 1990, 2000, 2010, 2020, 2023]
birth_rates = [4.53, 2.93, 1.59, 1.19, 1.03, 0.84, 0.72]

plt.figure(figsize=(10, 6))
plt.plot(years, birth_rates, marker='o')
plt.title('Total Fertility Rate in South Korea (1970-2023)', fontsize=16, fontproperties=fontprop)
plt.xticks(years)
plt.grid()

plt.savefig('output.png')
plt.close()
