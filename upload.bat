envs.bat
python -m build
py -m twine upload -p %pytok% -u "__token__" dist\lokzz*