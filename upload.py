from sshdata import SSHData
import os

class Upload():

	def __init__( self, sshinfo ):

		self.__dst_master_dir = './ws/'
		self.__src_master_dir = './upload_file/'
		self.__instance_ssh = SSHData(sshinfo[ 'hostip' ], sshinfo[ 'port' ], sshinfo[ 'username' ], sshinfo[ 'password' ])
		
	def upload_file( self, src_dir, dst_dir ):

		for item in os.listdir( src_dir ):

			cur_dst_item = os.path.join( dst_dir, item )
			cur_src_item = os.path.join( src_dir, item )

			if os.path.isdir( cur_src_item ):
				self.__instance_ssh.sshclient_execmd( 'mkdir ' + cur_dst_item )
				self.upload_file( cur_src_item, cur_dst_item )

			elif os.path.isfile( cur_src_item ):
				self.__instance_ssh.put_server_file( cur_src_item, cur_dst_item )

	def upload_all( self ):

		self.__instance_ssh.sshclient_execmd( 'mkdir ' + self.__dst_master_dir )
		self.upload_file( self.__src_master_dir, self.__dst_master_dir )
		self.__instance_ssh.ssh_close()


def main():

	sshinfo =  { 'hostname' : '', 'hostip' : '',
			'port':, 'username' : '', 'password' : '' }

	Upload(sshinfo).upload_all()


if __name__ == '__main__':

	main()
