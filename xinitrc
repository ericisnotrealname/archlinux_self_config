
# fcitx
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx
export SDL_IM_MODULE=fcitx
export GLFW_IM_MODULE=fcitx
fcitx5 &

# dwm_bar
/home/linye/.local/applications/dwm/dwm-bar/dwm_bar.sh &

# background picture
nitrogen --restore
# aria2c --conf-path=/home/linye/.config/aria2/aria2.conf &
exec dwm
