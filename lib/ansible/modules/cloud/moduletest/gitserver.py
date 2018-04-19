#!/usr/bin/python

import os
import sys
from ansible.module_utils.basic import AnsibleModule

def create_git_user(mod):

	git_username = mod.params['gitusername']
	project_name = mod.params['projectname']
	mod.fail_json(msg='Data recieved')

def main():

	mod=AnsibleModule(
			argument_spec=dict(
				gitusername=dict(default='user'),
				projectname=dict(required=True)
				)
			)

	create_git_user(mod)

if __name__ == '__main__':
	main()
