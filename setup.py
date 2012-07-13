from setuptools import setup, find_packages

package_data = ['templates/bsproject/*.html', 'static/bsproject/js/*', 'static/bsproject/css/*',
                'static/bsproject/img/*']
dependencies = ['Markdown==2.0.3']
# Untested below... 
# dependency_links = ['https://github.com/jmichalicek/django-taxonomies/zipball/master#egg=django-taxonomies1.0']
setup(name = "bsproject",
      version = "0.0.1",
      description = "A django app for displaying software development projects intended to work with bsblog",
      author = "Justin Michalicek",
      author_email = "jmichalicek@gmail.com",
      license = "www.opensource.org/licenses/bsd-license.php",
      packages = find_packages(),
      #'package' package must contain files (see list above)
      package_data = {'bsproject' : package_data },
      install_requires = dependencies,
      long_description = 'A django app for displaying software development projects intended to work with bsblog' 
)
