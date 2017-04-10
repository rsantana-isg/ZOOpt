"""
The class Parameter was implemented in this file.
A Parameter instance should be a necessary parameter to opt in RacosOptimization

Author:
    Yu-Ren Liu

"""

"""
 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU General Public License
 as published by the Free Software Foundation; either version 2
 of the License, or (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program; if not, write to the Free Software
 Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

 Copyright (C) 2017 Nanjing University, Nanjing, China
"""

import sys


class Parameter:

    def __init__(self, objective=None, budget=0, autoset=True):
        self.__budget = budget
        self.__train_size = 0
        self.__positive_size = 0
        self.__negative_size = 0
        self.__probability = 0.99
        if budget != 0 and autoset is True:
            self.auto_set(budget)

    # Set train_size, positive_size, negative_size by following rules:
    # budget < 3 ->> error
    # budget: 4-50 ->> train_size = 4, positive_size = 1
    # budget: 51-100 ->> train_size = 6, positive_size = 1
    # budget: 101-1000 ->> train_size = 12, positive_size = 2
    # budget > 1001 ->> train_size = 22, positive_size = 2
    def auto_set(self, budget):
        if budget < 3:
            print 'budget too small'
            sys.exit(1)
        elif budget <= 50:
            self.__train_size = 4
            self.__positive_size = 1
        elif budget <= 100:
            self.__train_size = 6
            self.__positive_size = 1
        elif budget <= 1000:
            self.__train_size = 12
            self.__positive_size = 2
        else:
            self.__train_size = 22
            self.__positive_size = 2
        self.__negative_size = self.__train_size - self.__positive_size

    def set_objective(self, objective):
        self.__objective = objective

    def set_budget(self, budget):
        self.__budget = budget

    def set_train_size(self, size):
        self.__train_size = size
        return

    def set_positive_size(self, size):
        self.__positive_size = size
        return

    def set_negative_size(self, size):
        self.__negative_size = size
        return

    def set_probability(self, probability):
        self.__probability = probability

    def get_objective(self):
        return self.__objective

    def get_budget(self):
        return self.__budget

    def get_train_size(self):
        return self.__train_size

    def get_positive_size(self):
        return self.__positive_size

    def get_negative_size(self):
        return self.__negative_size

    def get_probability(self):
        return self.__probability
