# Starship
eval "$(starship init zsh)"

# Auto-Complete
autoload -Uz compinit
compinit

# UV Config
export UV_LINK_MODE=copy

# UV Auto-Completion
eval "$(uv generate-shell-completion zsh)"

# Activate VENV on CD
# autoload -U add-zsh-hook
# activate-venv() {
#   local python_project="pyproject.toml"
#   local dot_venv_path=".venv"
#   local dot_venv_activate_path=".venv/bin/activate"

#   if [ -f "$python_project" ]; then
#     if [ -d "$dot_venv_path" ]; then
#       echo "Activating virtual environment..."
#       source $dot_venv_activate_path
#     else
#       echo "Creating virtual environment..."
#       uv venv
#     fi
#   fi
# }
# add-zsh-hook chpwd activate-venv
# activate-venv