# main_script.py
import matplotlib.pyplot as plt

# Import data from industries.py
from industries import auto_industry, auto_indautomate, auto_indhuman

# Remove '%' and convert to numerical values
auto_indautomate_values = [float(value.strip('%')) / 100 for value in auto_indautomate]
auto_indhuman_values = [float(value.strip('%')) / 100 for value in auto_indhuman]

# Perform calculations (e.g., average automation and human involvement)
avg_automation = sum(auto_indautomate_values) / len(auto_indautomate_values)
avg_human_involvement = sum(auto_indhuman_values) / len(auto_indhuman_values)

# Use the data in a bar chart
categories = auto_industry
plt.bar(categories, auto_indautomate_values, label='Automation')
plt.bar(categories, auto_indhuman_values, label='Human', bottom=auto_indautomate_values)

plt.xlabel('Industry')
plt.ylabel('Percentage')
plt.title('Automation vs Human Involvement')
plt.legend()
plt.show()
