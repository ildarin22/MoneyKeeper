"use strict";
/**
 * __author__ = 'ilov3'
 */
function AddAccountController($uibModalInstance, AddModalSvc, dataSvc, update) {
    AddModalSvc.name = 'Account';
    AddModalSvc.modalInstance = $uibModalInstance;
    AddModalSvc.resource = dataSvc.account;
    AddModalSvc.updateFunc = update;
    this.service = AddModalSvc;
    this.formFields = [
        {
            key: 'name',
            type: 'input',
            templateOptions: {
                type: 'text',
                label: 'Name',
                placeholder: '',
                required: true
            }
        },
        {
            key: 'opening',
            type: 'input',
            defaultValue: 0,
            templateOptions: {
                type: 'number',
                label: 'Opening',
                placeholder: '',
                required: true
            }
        },
        {
            key: 'addAnother',
            type: 'checkbox',
            templateOptions: {
                label: 'Add another',
                required: false
            }
        }
    ]
}

angular.module('MoneyKeeper.states').controller('AddAccountController', ['$uibModalInstance', 'AddModalSvc', 'dataSvc', 'update', AddAccountController]);