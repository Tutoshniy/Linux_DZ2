import subprocess


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(result.stdout)
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def test_step1():
    # test1
    res1 = checkout("cd {}; 7z a {}/arx2".format('/home/user/tst', '/home/user/tst'), "Everything is Ok")
    res2 = checkout("ls {}".format('/home/user/tst/arx2.7z'), "arx2.7z")
    assert res1 and res2, "test1 FAIL"


def test_step2():
    # test2
    res1 = checkout("cd {}; 7z e arx2.7z -o{} -y".format('/home/user/tst', '/home/user/result'), "Everything is Ok")
    res2 = checkout("ls {}".format('/home/user/result/test1'), "test1")
    res3 = checkout("ls {}".format('/home/user/result/test2'), "test2")
    assert res1 and res2 and res3, "test2 FAIL"


def test_step3():
    # test3
    res1 = checkout('cd {}; 7z u arx2.7z'.format('/home/user/tst'), "Everything is Ok"), "test3 FAIL"
    assert res1, "test3 FAIL"


def test_step4():
    # test4
    res1 = checkout('cd {}; 7z d arx2.7z'.format('/home/user/tst'), "Everything is Ok"), "test4 FAIL"
    assert res1, "test4 FAIL"


def test_step5():
    # test5
    res1 = checkout('cd {}; 7z l arx2.7z'.format('/home/user/result'), "2 files"), "test5 FAIL"
    assert res1, "test5 FAIL"


def test_step6():
    # test6
    res1 = checkout('cd {}; 7z x arx2.7z'.format('/home/user/result'), "Everything is Ok"), "test6 FAIL"
    res2 = checkout("ls {}".format('/home/user/result/test1'), "test1")
    res3 = checkout("ls {}".format('/home/user/result/test2'), "test2")
    assert res1 and res2 and res3, "test6 FAIL"
