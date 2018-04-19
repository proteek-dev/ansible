#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def save_data(mod):

	mod.fail_json(msg='Data recieved')

def main():

	mod=AnsibleModule(
			argument_spec=dict(
				url=dict(required=True),
				dest=dict(default='/tmp/fristmod.txt')
				)
			)

	save_data(mod)

if __name__ == '__main__':
	main()
