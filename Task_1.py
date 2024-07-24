
import matplotlib.pyplot as plt
import pandas as pd

age_data = {
    'Age': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'Frequency': [100, 200, 350, 450, 300, 200, 150, 100, 50, 25]
}

gender_data = {
    'Gender': ['Male', 'Female', 'Other'],
    'Frequency': [400, 450, 50]
}

civil_status_data = {
    'Civil Status': ['Single', 'Married', 'Divorced', 'Widowed'],
    'Frequency': [300, 500, 100, 50]
}

nationality_data = {
    'Nationality': ['USA', 'UK', 'Canada', 'Australia', 'India', 'China'],
    'Frequency': [250, 200, 150, 100, 300, 400]
}

province_population_data = {
    'Province': ['Province A', 'Province B', 'Province C', 'Province D'],
    'Population': [500000, 700000, 400000, 600000]
}

marital_status_data = {
    'Country': ['USA', 'UK', 'Canada', 'Australia', 'India', 'China'],
    'Single': [150, 100, 80, 70, 200, 250],
    'Married': [200, 150, 120, 100, 250, 300],
    'Divorced': [50, 30, 20, 10, 50, 100],
    'Widowed': [20, 20, 10, 0, 20, 50]
}

plt.figure(figsize=(10, 6))
plt.hist(age_data['Age'], bins=10, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

gender_df = pd.DataFrame(gender_data)
plt.figure(figsize=(8, 5))
plt.bar(gender_df['Gender'], gender_df['Frequency'], color=['blue', 'pink', 'purple'])
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

civil_status_df = pd.DataFrame(civil_status_data)
plt.figure(figsize=(8, 5))
plt.bar(civil_status_df['Civil Status'], civil_status_df['Frequency'], color='orange')
plt.title('Civil Status Distribution')
plt.xlabel('Civil Status')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

nationality_df = pd.DataFrame(nationality_data)
plt.figure(figsize=(8, 5))
plt.bar(nationality_df['Nationality'], nationality_df['Frequency'], color='green')
plt.title('Nationality Distribution')
plt.xlabel('Nationality')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

province_population_df = pd.DataFrame(province_population_data)
plt.figure(figsize=(8, 5))
plt.bar(province_population_df['Province'], province_population_df['Population'], color='purple')
plt.title('Population Distribution Across Provinces')
plt.xlabel('Province')
plt.ylabel('Population')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

marital_status_df = pd.DataFrame(marital_status_data)
marital_status_df.set_index('Country', inplace=True)
marital_status_df.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Marital Status Distribution in Different Countries')
plt.xlabel('Country')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()





