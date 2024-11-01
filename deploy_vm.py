from pyVmomi import vim
import utils
import json

def deploy_vm(content, ova_path, vm_name):
    # Accès au dossier des VMs et aux ressources
    vm_folder = content.rootFolder.childEntity[0].vmFolder
    resource_pool = content.rootFolder.childEntity[0].hostFolder.childEntity[0].resourcePool

    # Déploiement en utilisant l'OVA
    ova_import_spec = vim.Ova.OvaImportSpec()
    ova_import_spec.ovfDescriptor = ova_path

    task = vm_folder.ImportVApp(ova_import_spec, resource_pool)
    return task
    
def main():
    content = utils.connect()

    # Charger la configuration
    utils.load_config('config.json')

    for vm_config in config['deploy_vm']:
        deploy_vm(content, vm_config['ova_path'], vm_config['name'])
        
        
if __name__ == '__main__':
    main()
