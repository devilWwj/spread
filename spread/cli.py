#-*- coding: utf-8 -*-
import sys

from spread.commands import TestCommand
from spread.commands import CrawlerCommand, Scel2TxtCommand, BEMSCommand
from spread.commands import SpreadCommand, SpreadShortCutCommand
from spread.commands import BEMSCountCommand
from spread.commands import SpreadServerCommand


class CLI(object):

    default_commands = (TestCommand,
                        CrawlerCommand, Scel2TxtCommand, BEMSCommand,
                        SpreadCommand, SpreadShortCutCommand,
                        BEMSCountCommand, SpreadServerCommand)

    def __init__(self, commands=()):
        self.commands = dict()
        self.command_instances = list()

        for c in self.default_commands:
            self.add_command(c)

        for c in commands:
            self.add_command(c)

    def add_command(self, command_cls):
        command_instance = command_cls()
        self.command_instances.append(command_instance)
        self.commands[command_instance.command] = command_instance

    def execute(self, command_str, args):
        executor = self.commands[command_str]
        executor.set_args(args)
        executor.do()

    def run(self):
        args = sys.argv
        if not len(args) > 1:
            print "Please input your command."
            for command in self.command_instances:
                print command.command, command.args_table
            return None

        cmd = args[1]
        cmd_args = args[2:]
        self.execute(cmd, cmd_args)
