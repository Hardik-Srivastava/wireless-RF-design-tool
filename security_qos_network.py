class SecurityMeasures:
    def __init__(self, encryption_protocol, authentication_method):
        self.encryption_protocol = encryption_protocol
        self.authentication_method = authentication_method

    def configure_security(self):
        print("Configuring security measures...")
        print("Encryption Protocol:", self.encryption_protocol)
        print("Authentication Method:", self.authentication_method)

class QualityOfService:
    def __init__(self, traffic_prioritization):
        self.traffic_prioritization = traffic_prioritization

    def configure_qos(self):
        print("Configuring Quality of Service (QoS)...")
        print("Traffic Prioritization:", self.traffic_prioritization)

class NetworkManagement:
    def __init__(self, centralized_management):
        self.centralized_management = centralized_management

    def manage_network(self):
        print("Managing network...")
        if self.centralized_management:
            print("Using centralized management system.")
        else:
            print("Managing network locally.")

