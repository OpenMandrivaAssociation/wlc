name=$(cat *.spec | grep -i Name: | awk '{print $NF}')
repo_url=$(cat *.spec | grep -i Url: | awk '{print $NF}')
version=$(cat *.spec | grep -i Version: | awk '{print $NF}')
git clone $repo_url/${name}.git $name
pushd $name
git archive --format=tar --prefix $name-$version-$(date +%Y%m%d)/ HEAD | xz -vf > ../$name-$version-$(date +%Y%m%d).tar.xz
popd
