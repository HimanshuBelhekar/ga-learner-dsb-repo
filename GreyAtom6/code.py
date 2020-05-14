# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()

plt.bar(loan_status.index,loan_status)
#Code starts here


# --------------
#Code starts here

property_and_loan = data.groupby(['Property_Area','Loan_Status'])

property_and_loan = property_and_loan.size().unstack()

property_and_loan.plot(kind='bar',stacked=False,rot=45)

plt.xlabel('Property Area')
plt.ylabel('Loan Status')


# --------------
#Code starts here
education_and_loan = data.groupby(['Education','Loan_Status'])
education_and_loan = education_and_loan.size().unstack()

education_and_loan.plot(kind='bar',stacked=True,rot=45)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')


# --------------
#Code starts here

graduate = data[data['Education'] == 'Graduate']

not_graduate = data[data['Education'] == 'Not Graduate']

graduate['LoanAmount'].plot(kind='density',label='Graduate')

not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')





#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig, (ax_1,ax_2,ax_3) = plt.subplots(nrows=3,ncols=1)

ax_1 = data.plot.scatter(x='ApplicantIncome',y='LoanAmount')
ax_1.set_title('Applicant Income')

ax_2 = data.plot.scatter(x='CoapplicantIncome',y='LoanAmount')
ax_1.set_title('Coapplicant Income')

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
ax_3 = data.plot.scatter(x='TotalIncome',y='LoanAmount')
ax_3.set_title('Total Income')

