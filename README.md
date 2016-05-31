# openfst

- description
  - test code for openfst

- open fst references
  - [source](http://www.openfst.org/twiki/bin/view/FST/FstDownload)
  - [quick start](http://www.openfst.org/twiki/bin/view/FST/FstQuickTour)
  - [python extention](http://www.openfst.org/twiki/bin/view/FST/PythonExtension)

- install
```
$ cd ~/openfst-1.5.3
$ ./configure --enable-python ; make ; make install
$ apt-get install graphviz
```
- test
```
./test.sh -v -v
```
