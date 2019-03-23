# 掃き出し法
import numpy as np
import sys


class SimultaneousEquation:
    """連立方程式"""

    def __init__(self, input_data):
        self._matrix = input_data

    def sweeping_method(self):
        """掃き出し法"""
        for i in range(len(self._matrix)):
            if np.all(self._matrix[i][:i]>0):
                for v in range(len(self._matrix[i][:i])):
                    self._matrix[i] = self._matrix[i] - self._matrix[v]*self._matrix[i][v]
            if self._matrix[i][i] != 1:
                self._matrix[i] = self._matrix[i]/self._matrix[i][i]
        return self._matrix       


if __name__=='__main__':
    args = sys.argv
    x = np.random.randint(1, 10, (8,9))  # 1~20までの値で?x?行列
    # x = args[1] 
    simultaneous_equation = SimultaneousEquation(x)
    x = simultaneous_equation.sweeping_method() 
    print(x+0.)  # -0が出力をプラスの符号に変換
    
