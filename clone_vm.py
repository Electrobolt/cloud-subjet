from pyVmomi import vim
import utils
import json

def clone_vm(content, source_vm_name, clone_name):
    # Vérification de la présence de la VM à cloner
    vm = content.searchIndex.FindByDnsName(dnsName=source_vm_name, vmSearch=True)
    if not vm:
        print(f"VM '{source_vm_name}' non trouvée.")
        return

    clone_spec = vim.vm.CloneSpec()
    task = vm.Clone(folder=vm.parent, name=clone_name, spec=clone_spec)
    return task
    
def main():
    content = utils.connect()

    # Charger la configuration
    utils.load_config('config.json')

    for clone_config in config['clone_vms']:
        for i in range(clone_config['count']):
            clone_vm(content, clone_config['source_name'], f"{clone_config['name']}_{i + 1}")
        
        
if __name__ == '__main__':
    main()
