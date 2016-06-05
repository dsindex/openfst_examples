# openfst

- description
  - test code for openfst

- open fst references
  - [source](http://www.openfst.org/twiki/bin/view/FST/FstDownload)
  - [quick start](http://www.openfst.org/twiki/bin/view/FST/FstQuickTour)
  - [tutorial](http://www.openfst.org/twiki/bin/view/FST/FstSltTutorial)
  - [python extention](http://www.openfst.org/twiki/bin/view/FST/PythonExtension)
  - [edit distance using fst](http://www.tylerpalsulich.com/blog/2015/05/17/levenshtein-edit-distance-with-fsts/)
  - [lm to fst](https://williamhartmann.wordpress.com/2014/02/02/converting-a-language-model-to-a-finite-state-transducer/)
  - [edit distance automata](http://blog.notdot.net/2010/07/Damn-Cool-Algorithms-Levenshtein-Automata)

- install
```
$ cd ~/openfst-1.5.3
(for testing pywrapfst)
$ ./configure --enable-python ; make ; make install
(for testing pyfst, do not use pywrapfst)
$ ./configure ; make ; make install ; CFLAGS="-std=c++0x" pip install pyfst
$ apt-get install graphviz
```
- test
```
* all code from above references
./basic.sh -v -v
./edit_distance.sh -v -v
```

- note
```
ㅡpyfst를 사용해서 edit distance automata
  구현해보고 단어 후보를 찾아보자
  : 사전피딩은 trie 사용

ㅡ또한 lm을 fst로 변환한 다음
  두개의 fst의 shortest path 탐색
  가장 적합한 segmentation을 구한다
  : lm구축 단위는 사전단위로 해야한다
  : 입력단어의 fst는 모든 가능한 segmentation
    고려해서 만든다
    aword -> a w o r d
             a wo rd
             a wor d
             a word
             ....
    fsa로 만든다!

ㅡcompositon
  a:b , b:c
  이런 케이스에 대해서만 가능하다
  결국 abc.fst, t.fst, cba.fst를 compose하면
  a -> b -> c + 임의경로 + c -> b -> a
  여기서
  a:c -> b:b -> c:a
  이러한 transducer가 만들어지는 것
  이것의 shortest path가 edit distance
  lm에서도 비슷한데
  word.fsa lm.fst를 compose하면
  결국 lm.fst에서 word.fsa에 한정된 automata만
  남게된다. 여기서 shortest path를 찾으면 그게
  결국 best segmentation이 되는 셈이다.

ㅡ일반적인 방법론을 사용하는 것도 좋지만
  fst는 매우 적용범위가 광범위하다.
  fst를 이용한 문제풀이를 많이 해두면 좋을듯~
```
