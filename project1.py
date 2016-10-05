import numpy as np
import matplotlib.pyplot as plt
import xlrd
print "UBitName = guanyuly"
print "personNumber = 50208193"
workbook=xlrd.open_workbook("university data.xlsx")
sheet=workbook.sheet_by_index(0)
te1=[]
te2=[]
te3=[]
te4=[]
for i in range(1,50):
    te1.extend([sheet.cell_value(i,2)])
    te2.extend([sheet.cell_value(i,3)])
    te3.extend([sheet.cell_value(i,4)])
    te4.extend([sheet.cell_value(i,5)])
cs_score=np.array(te1)
research=np.array(te2)
admin=np.array(te3)
tuition=np.array(te4)
mu1=np.mean(cs_score)
mu2=np.mean(research)
mu3=np.mean(admin)
mu4=np.mean(tuition)
var1=np.var(cs_score)
var2=np.var(research)
var3=np.var(admin)
var4=np.var(tuition)
sigma1=np.std(cs_score)
sigma2=np.std(research)
sigma3=np.std(admin)
sigma4=np.std(tuition)
print "mu1 =",round(mu1,3)
print "mu2 =",round(mu2,3)
print "mu3 =",round(mu3,3)
print "mu4 =",round(mu4,3)
print "var1 =",round(var1,3)
print "var2 =",round(var2,3)
print "var3 =",round(var3,3)
print "var4 =",round(var4,3)
print "sigma1 =",round(sigma1,3)
print "sigma2 =",round(sigma2,3)
print "sigma3 =",round(sigma3,3)
print "sigma4 =",round(sigma4,3)
x=np.matrix([cs_score,research,admin,tuition])
covarianceMat=np.cov(x)
correlationMat=np.corrcoef(x)
print '''covarianceMat =
''',covarianceMat
print '''correlationMat =
''',correlationMat
plt.figure(1)
plt.plot(cs_score,research,"o")
plt.xlabel('cs_score')
plt.ylabel('research')
plt.show()
plt.figure(2)
plt.plot(cs_score,admin,"o")
plt.xlabel('cs_score')
plt.ylabel('admin')
plt.show()
plt.figure(3)
plt.plot(cs_score,tuition,"o")
plt.xlabel('cs_score')
plt.ylabel('tuition')
plt.show()
plt.figure(4)
plt.plot(research,admin,"o")
plt.xlabel('research')
plt.ylabel('admin')
plt.show()
plt.figure(5)
plt.plot(research,tuition,"o")
plt.xlabel('research')
plt.ylabel('tuition')
plt.show()
plt.figure(6)
plt.plot(admin,tuition,"o")
plt.xlabel('admin')
plt.ylabel('tuition')
plt.show()
def loglikelihood(a,mean,std):
    sum=0
    for i in range(0,49):
        sum=sum+(a[i]-mean)*(a[i]-mean)
    return -49.0/2.0*np.log(2*np.pi)-49.0/2.0*np.log(std*std)-0.5/(std*std)*sum
logLikelihood=loglikelihood(cs_score,mu1,sigma1)+loglikelihood(research,mu2,sigma2)+loglikelihood(admin,mu3,sigma3)+loglikelihood(tuition,mu4,sigma4)
print "logLikelihood =",logLikelihood
B=np.matrix([[0,0,0,0],[1,0,0,0],[0,0,0,1],[1,0,0,0]])
print '''BNgraph =
''',B
x0=np.zeros(49)
for i in range(0,49):
    x0[i]=1
def mysum(a,b):
    sum=0
    for i in range(0,49):
        sum=sum+a[i]*b[i]
    return sum
A1=np.zeros((3,3))
A1[0,0]=mysum(x0,x0)
A1[0,1]=mysum(x0,research)
A1[0,2]=mysum(x0,tuition)
A1[1,0]=mysum(research,x0)
A1[1,1]=mysum(research,research)
A1[1,2]=mysum(research,tuition)
A1[2,0]=mysum(tuition,x0)
A1[2,1]=mysum(tuition,research)
A1[2,2]=mysum(tuition,tuition)
y1=np.zeros((3,1))
y1[0,0]=mysum(x0,cs_score)
y1[1,0]=mysum(research,cs_score)
y1[2,0]=mysum(tuition,cs_score)
beta1=np.linalg.solve(A1,y1)
sum=0
for i in range(0,49):
    sum=sum+np.power((beta1[0,0]*x0[i]+beta1[1,0]*research[i]+beta1[2,0]*tuition[i]-cs_score[i]),2)
sig1=sum/49
sum=0
for i in range(0,49):
    sum=sum-0.5*np.log(2*np.pi*sig1)-0.5/sig1*np.power((beta1[0,0]*x0[i]+beta1[1,0]*research[i]+beta1[2,0]*tuition[i]-cs_score[i]),2)
re1=sum
A2=np.zeros((2,2))
A2[0,0]=mysum(x0,x0)
A2[0,1]=mysum(x0,admin)
A2[1,0]=mysum(admin,x0)
A2[1,1]=mysum(admin,admin)
y2=np.zeros((2,1))
y2[0,0]=mysum(x0,tuition)
y2[1,0]=mysum(admin,tuition)
beta3=np.linalg.solve(A2,y2)
sum=0
for i in range(0,49):
    sum=sum+np.power((beta3[0,0]*x0[i]+beta3[1,0]*admin[i]-tuition[i]),2)
sig2=sum/49
sum=0
for i in range(0,49):
    sum=sum-0.5*np.log(2*np.pi*sig2)-0.5/sig2*np.power((beta3[0,0]*x0[i]+beta3[1,0]*admin[i]-tuition[i]),2)
re2=sum
BNloglikelihood=re1+loglikelihood(research,mu2,sigma2)+loglikelihood(admin,mu3,sigma3)+re2
print "BNloglikelihood =",BNloglikelihood

