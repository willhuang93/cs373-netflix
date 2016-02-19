#!/usr/bin/env python3

# -------------------------------
# projects/Netflix/TestNetflix.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Netflix import netflix_eval, netflix_solve, RMSE, netflix_print

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = netflix_eval(2003, 3.749542961608775, 3.6451612903225805)
        self.assertEqual(v, 3.7665670574312426)

    def test_eval_2 (self) :
        v = netflix_eval(2002 ,  3.2842105263157895 ,  3.0 )
        self.assertEqual(v, 2.681073331815676)

    def test_eval_3 (self) :
        v = netflix_eval(2001, 3.4473684210526314, 2.981818181818182)
        self.assertEqual(v, 2.9010494083707)

    def test_eval_4 (self) :
        v = netflix_eval(2004 ,  3.2453531598513012 ,  3.967479674796748)
        self.assertEqual(v, 3.5596956401479356)

    def test_eval_5 (self) :
        v = netflix_eval(2000 ,  2.5385906040268456 ,  3.2074468085106385)
        self.assertEqual(v, 2.2179002180373706)

    def test_eval_6 (self) :
        v = netflix_eval(1989 ,  3.117071260767424 ,  3.6075388026607538)
        self.assertEqual(v, 3.226472868928064)

    def test_eval_7 (self) :
        v = netflix_eval(1981 ,  2.467289719626168 ,  3.614)
        self.assertEqual(v, 2.5531525251260545)

    def test_eval_8 (self) :
        v = netflix_eval(1980 ,  2.9591836734693877 ,  4.222222222222222)
        self.assertEqual(v, 3.7532687011914962)

    def test_eval_9 (self) :
        v = netflix_eval(1974 ,  2.9099264705882355 ,  3.4166666666666665)
        self.assertEqual(v, 2.9484559427547885)

    def test_eval_10 (self) :
        v = netflix_eval(1970 ,  3.892605484336531 ,  4.0606060606060606)
        self.assertEqual(v, 4.625074350442478)

    def test_eval_11 (self) :
        v = netflix_eval(1962 ,  3.9075484354654146 ,  3.6053639846743293)
        self.assertEqual(v, 4.234775225639631)

    def test_eval_12 (self) :
        v = netflix_eval(1957 ,  4.040349417637271 ,  2.576923076923077)
        self.assertEqual(v, 3.3891353000602344)

    def test_eval_13 (self) :
        v = netflix_eval(1953 ,  3.8604769152714358 ,  4.286549707602339)
        self.assertEqual(v, 4.968889428373661)

    def test_eval_14 (self) :
        v = netflix_eval(1946 ,  3.7259450171821307 ,  4.116483516483516)
        self.assertEqual(v, 4.714291339165532)

    def test_eval_15 (self) :
        v = netflix_eval(1942 ,  3.6823361823361824 ,  3.539473684210526)
        self.assertEqual(v, 4.103672672046596)

    def test_eval_16 (self) :
        v = netflix_eval(1934 ,  4.011271389359341 ,  2.9759036144578315)
        self.assertEqual(v, 3.8790378093170585)

    def test_eval_17 (self) :
        v = netflix_eval(1925 ,  3.4804748516088724 ,  3.6288998357963873)
        self.assertEqual(v,    4.011237492905146)

    def test_eval_18 (self) :
        v = netflix_eval(1915 ,  3.321243523316062 ,  4.534653465346534  )
        self.assertEqual(v,  4.767759794162482)

    def test_eval_19 (self) :
        v = netflix_eval(1909 ,  2.7889908256880735 ,  3.9051094890510947   )
        self.assertEqual(v, 3.6159631202390545)

    def test_eval_19 (self) :
        v = netflix_eval(1909 ,  2.7889908256880735 ,  3.9051094890510947   )
        self.assertEqual(v, 3.6159631202390545)

    def test_eval_19 (self) :
        v = netflix_eval(1955, 0, 0)
        self.assertEqual(v, 0)


    # 3.2281371945001136

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        netflix_print(w, 1, {1 : [1, 2]})
        self.assertEqual(w.getvalue(), "1:\n1\n2\nRMSE: 1")

    def test_print_2 (self) :
        w = StringIO()
        netflix_print(w, 0, {1 : [1, 1]})
        self.assertEqual(w.getvalue(), "1:\n1\n1\nRMSE: 0")

    def test_print_3 (self) :
        w = StringIO()
        netflix_print(w, 4, {5 : [1, 2, 3, 4]})
        self.assertEqual(w.getvalue(), "5:\n1\n2\n3\n4\nRMSE: 4")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1:\n317050\n1027056\n1394012\n548064\n1394012\n1406595\n2529547\n1682104\n2625019\n1774623\n470861\n712610\n1772839\n1059319\n2380848\n548064\n2647871")
        w = StringIO()
        a = netflix_solve(r, w)
        boo = 0
        if a < 1:
            boo = 1
        self.assertEqual(boo, 1)

# ----
# main
# ----

if __name__ == "__main__" :
    main()