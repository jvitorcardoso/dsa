FROM gitpod/workspace-full
RUN brew install scala

RUN pyenv install 3.11 \
    && pyenv global 3.11