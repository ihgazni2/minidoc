pip3 uninstall minidoc
git rm -r dist
git rm -r build
git rm -r minidoc.egg-info
rm -r dist
rm -r build
rm -r minidoc.egg-info
git add .
git commit -m "remove old build"
