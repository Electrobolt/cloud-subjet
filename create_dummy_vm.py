from pyVmomi import vim
import utils
import json

def create_dummy_vm(vm_config, content, vm_folder, resource_pool):

    # Configuration de la VM
    vm_spec = vim.VirtualMachineConfigInfo()
    vm_spec.name = vm_config['name']
    vm_spec.memoryMB = vm_config['memoryMB']
    vm_spec.numCPUs = vm_config['numCPUs']
    vm_spec.guestId = 'otherGuest' # ID du système d'exploitation invité
    
    # Accès au dossier et au pool de ressources
    vm_folder = content.rootFolder.childEntity[0].vmFolder
resource_pool = content.rootFolder.childEntity[0].hostFolder.childEntity[0].resourcePool
datastore = vm_config['datastore']

    # Création de la VM
    task = vm_folder.CreateVM_Task(config=vm_spec, pool=resource_pool)
    return task
    
    
def main():
    content = utils.connect()

    # Charger la configuration
    utils.load_config('config.json')

    for vm_config in config['create_vms']:
        create_dummy_vm(vm_config, content, vm_folder, resource_pool)
        
        
if __name__ == '__main__':
    main()
