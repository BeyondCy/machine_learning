# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def loadDataSet(fileName):
    """
        函数说明:加载数据
        Parameters:
        fileName - 文件名
        Returns:
        xArr - x数据集
        yArr - y数据集
        Website:
        
        Modify:
        2018-02-10
        """
    
    numFeat = len(open(fileName).readline().split('\t')) - 1
    print 'numFeat: ', numFeat
    xArr = []; yArr = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        xArr.append(lineArr)
        yArr.append(float(curLine[-1]))
#    print xArr
#    print yArr
    return xArr, yArr

def standRegression(xArr, yArr):
    """
    Description:
        根据推导出来的正规方程组来计算回归系数
    Parameters:
        xArr - x数据集
        yArr - y数据集
    Returns:
        ws - 回归系数
    """
#   x矩阵
    xMat = np.mat(xArr);
#   y矩阵转置
    yMat = np.mat(yArr).T;
    xTx = xMat.T * xMat;
#   判断矩阵是否可求逆:采用linalg.det计算行列式的方式，如果行列式的值为0，那么矩阵不可逆
    if np.linalg.det(xTx) == 0.0:
        print ("矩阵为奇异矩阵，不可求逆")
        return
    ws = xTx.I * (xMat.T * yMat);
    return ws;


def plotRegression():
    """
    """
    xArr, yArr = loadDataSet('ex0.txt');  #加载数据集
    ws = standRegression(xArr, yArr);   #计算回归系数
    xMat = np.mat(xArr)   #创建xMat矩阵
    yMat = np.mat(yArr)    #创建yMat矩阵
    xCopy = xMat.copy()      #深拷贝xMat矩阵
    xCopy.sort(0)       #排序，这里是为了避免直线上数据点次序混乱，导致绘图出现问题，所以这里将点按照升序进行排列
    yHat = xCopy * ws   #计算对应的y值
    fig = plt.figure()
    ax = fig.add_subplot(111)  #添加subplot
    ax.plot(xCopy[:, 1], yHat, c = 'red')                                #绘制回归曲线
    ax.scatter(xMat[:,1].flatten().A[0], yMat.flatten().A[0], s = 20, c = 'blue',alpha = .5)                #绘制样本点
    plt.title('DataSet')                                                #绘制title
    plt.xlabel('X')
    plt.show()


def plotDataSet():
    """
        函数说明:绘制数据集
        Parameters:
        无
        Returns:
        无
        Website:
        Modify:
        2018-02-10
        """
    xArr, yArr = loadDataSet('ex0.txt')                                    #加载数据集
    n = len(xArr)                                                        #数据个数
    print 'n: ', n
    xcord = []; ycord = []                                                #样本点
    for i in range(n):
        xcord.append(xArr[i][1]); ycord.append(yArr[i])                    #样本点
    fig = plt.figure()
    ax = fig.add_subplot(111)                                            #添加subplot
    ax.scatter(xcord, ycord, s = 20, c = 'green',alpha = .5)                #绘制样本点
    plt.title('DataSet')                                                #绘制title
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

if __name__ == '__main__':
    #   python中提供了相关系数的计算方法
    xArr, yArr = loadDataSet('ex0.txt')                                    #加载数据集
    ws = standRegression(xArr, yArr)                                        #计算回归系数
    xMat = np.mat(xArr)                                                    #创建xMat矩阵
    yMat = np.mat(yArr)                                                    #创建yMat矩阵
    yHat = xMat * ws
    print (np.corrcoef(yHat.T, yMat))
#    plotDataSet()
    plotRegression();








