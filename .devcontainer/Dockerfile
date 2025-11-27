FROM python:3-alpine

# Install basic development tools
RUN apk update
RUN apk add --no-cache sudo bash zsh git curl openssh-client starship just uv

# Update pip
RUN pip install --upgrade pip

# Set `DEVCONTAINER` environment variable to help with orientation
ENV DEVCONTAINER=true

# Set `SHELL` environment variable to use Zsh as the default shell
ENV SHELL=/bin/zsh

# Create `worker` user
RUN adduser -D worker && echo "worker ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Set user to `worker`
ENV PATH="/home/worker/.local/bin:${PATH}"

# Setup Zsh
COPY --chown=worker:worker ./.zshrc /home/worker/.zshrc

USER worker