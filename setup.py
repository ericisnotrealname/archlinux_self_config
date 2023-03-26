#!/usr/bin/python3
"""
set up to install package in archlinux
"""
import os
import yaml



class Installtion:
    """
    install packages
    """

    def __init__(self, config_file:str):
        with open(config_file, encoding="utf-8") as requirements:
            self.require_pkgs = yaml.load(requirements, Loader=yaml.FullLoader)

    def install_from_dict_value(self, pkg_dict:dict, installing=True):
        """
        install package from dict
        """
        for pkg_name, pkg in pkg_dict.items():
            print(f"{pkg_name}:")
            if isinstance(pkg, str):
                print(f"\t{pkg}")
                if installing:
                    os.popen(f"pacman -S {pkg} -y")
            elif isinstance(pkg, dict):
                self.install_from_dict_value(pkg_dict=pkg, installing=installing)
            elif isinstance(pkg, list):
                self.install_from_list_value(pkg_list=pkg, installing=installing)

    def install_from_list_value(self, pkg_list:list, installing=False):
        """
        install package from list
        """
        for pkg in pkg_list:
            if isinstance(pkg, str):
                print(f"\t{pkg}")
                if installing:
                    os.popen(f"pacman -S {pkg} -y")
            elif isinstance(pkg, list):
                self.install_from_list_value(pkg_list=pkg, installing=installing)
            elif isinstance(pkg, dict):
                self.install_from_list_value(pkg_list=pkg, installing=installing)

    def show_packages(self):
        """
        show packages from yaml
        """
        if isinstance(self.require_pkgs, dict):
            self.install_from_dict_value(self.require_pkgs, installing=False)
        elif isinstance(self.require_pkgs, list):
            self.install_from_list_value(self.require_pkgs, installing=False)

    def install_packages(self):
        """
        install packages from yaml
        """
        if isinstance(self.require_pkgs, dict):
            self.install_from_dict_value(self.require_pkgs, installing=True)
        elif isinstance(self.require_pkgs, list):
            self.install_from_list_value(self.require_pkgs, installing=True)


installtion = Installtion("./requirements.yaml")
installtion.install_packages()
