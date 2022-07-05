# hypermodern-python

[Reference](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)

## Setup

1. Install pyenv for managing python versions

```sh
curl https://pyenv.run | bash
```

vim /.bashrc

```sh
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Reload the shell: *source ~/.bashrc*

Get latest python
```sh
pyenv install 3.10.2

# Apply it
pyenv local 3.10.2

# Check it
python --version
```

## Install Poetry to manage python dependencies

```sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# Activate it
source ~/.poetry/env

# Initialize it
poetry init --no-interaction
```

Boom! *pyproject.toml* created.


## Setup folders

```sh
.
├── pyproject.toml
└── src
    └── hypermodern_python
        └── __init__.py

2 directories, 2 files
```
