#!/usr/bin/env bash
/usr/bin/setxkbmap -option "caps:swapescape"

# Path to the bash it configuration
export BASH_IT="${HOME}/.bash_it"

# Lock and Load a custom theme file
# location /.bash_it/themes/
export BASH_IT_THEME='bobby'

# Your place for hosting Git repos. I use this for private repos.
export GIT_HOSTING='git@github.com'

# Don't check mail when opening terminal.
unset MAILCHECK

# Set this to the command you use for todo.txt-cli
export TODO="t"

# Set this to false to turn off version control status checking within the prompt for all themes
export SCM_CHECK=true

# Set vcprompt executable path for scm advance info in prompt (demula theme)
# https://github.com/xvzf/vcprompt
#export VCPROMPT_EXECUTABLE=~/.vcprompt/bin/vcprompt

# Load Bash It
source $BASH_IT/bash_it.sh

[ -f ~/.fzf.bash ] && source ~/.fzf.bash

export BOOST_INSTALL=/usr/include/boost
export GMP_INSTALL=/usr/lib

# rbenv setup
# export RBENV_ROOT="$HOME/.rbenv"
# export PATH="$RBENV_ROOT/bin:$PATH"
# eval "$(rbenv init -)"

eval "$(direnv hook bash)"
