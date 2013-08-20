#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
SYNOPSIS

    .

DESCRIPTION
    

EXAMPLES
    
    python csv_io.py


EXIT STATUS
    
    0 program exit normal
    1 program had problem on execution


AUTHOR

    Theofilis George <theofilis.g@gmail.com>
    Skianis Konstantinos <rob.cs.aueb@gmail.com>

LICENSE

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

VERSION

    1
"""
import os
import pylzma
import pandas as pd

import warnings
warnings.filterwarnings('ignore',category=pd.io.pytables.PerformanceWarning)

def read_folder(storefilename, dir):
    files = [f for f in os.listdir('./' + dir) if os.path.isfile( os.path.join(dir, f) )]

    for f in files:
        with pd.get_store(storefilename) as store:
            id = f.replace(".csv", "")

            filename = os.path.join(dir, f)
            print 'Append file:', id
            

def main():

    read_folder('store.h5', 'weather')

    print store

    store.close()
if __name__ == '__main__':
    main()
