from pathlib import Path
import shutil
import os, stat

def make_dir_writable(function, path, exception):
    os.chmod(path, stat.S_IWRITE)
    function(path)

def delete_folder(path_str):
	p = Path(path_str)
	shutil.rmtree(p, onerror=make_dir_writable)

def delete_old_dotnet(basepath):
	p = Path(base_path)

	# achando as versões instaladas e adicionando em lista
	subdirectories = [x for x in p.iterdir() if x.is_dir()]
	versoes = []
	for s in subdirectories:
		versoes.append(s.__str__().split('\\')[-1])

	# deletando versoes antigas que começam com mesmo digito
	for v in versoes:
		for v2 in versoes:
			if v2 != v and v2[0] == v[0]:
				if v2 < v and os.path.exists(Path(basepath+'\\'+ v2)):
					delete_folder(base_path+'\\'+ v2)



#repositórios base dotnet
paths = ['C:\Program Files\dotnet\shared\\teste']
for path in paths:
	# rodando funcao
	delete_old_dotnet(base_path)