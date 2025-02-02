from helpers.modem_support.default import DefaultVendor


class Quectel(DefaultVendor):
    """
    Quectel vendor class that contains default parameters
    and methods of Quectel modules.
    """

    vendor_name = "Quectel"
    vid = "2c7c"

    interface_name = "usb0"
    mode_status_command = 'AT+QCFG="usbnet"'
    reboot_command = "AT+CFUN=1,1"
    pdp_activate_command = "AT"
    pdp_status_command = "AT+CGACT?"
    ecm_mode_setter_command = 'AT+QCFG="usbnet",1'
    ecm_mode_response = '"usbnet",1'
    ccid_command = "AT+ICCID"
    eps_mode_status_command='AT+QNVFW="/nv/item_files/modem/mmode/ue_usage_setting"'
    eps_mode_setter_command='AT+QNVFW="/nv/item_files/modem/mmode/ue_usage_setting",01'
    eps_data_centric_response="01"
