import os
import zipfile2

def test_zip():
    path_main = os.path.dirname(os.path.dirname(__file__))
    files_list = os.listdir(os.path.join(path_main, 'tests/resources'))
    with zipfile2.ZipFile(os.path.join(os.path.join(path_main, 'tmp'), "arhive_for_test"), 'w') as zf:
        for file in files_list:
            zf.write(os.path.join(os.path.join(path_main, 'resources')), file)
        for y in zf.namelist():
            assert y[:-1] in files_list