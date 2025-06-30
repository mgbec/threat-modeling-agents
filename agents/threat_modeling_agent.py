class ThreatModelingAgent:
    """
    Agent to identify threats in the architecture.
    """
    def model_threats(self, architecture_data):
        """
        Identifies threats in the architecture based on component types.

        Args:
            architecture_data (dict): The architecture data from the parser agent.

        Returns:
            list: A list of identified threats.
        """
        print("Modeling threats with enhanced logic...")
        threats = []
        
        # A simple knowledge base of threats for different component keywords.
        threat_definitions = {
            "internet-gateway": {"threat": "Internet Gateway is a potential single point of failure and a primary target for DDoS attacks.", "framework": "STRIDE", "category": "Denial of Service"},
            "load-balancer": {"threat": "Application Load Balancer may have misconfigured listeners or security groups, exposing backend services.", "framework": "MITRE ATT&CK", "category": "Initial Access"},
            "auto-scaling": {"threat": "Auto Scaling group misconfiguration could lead to resource exhaustion or insufficient capacity during an attack.", "framework": "STRIDE", "category": "Denial of Service"},
            "route53": {"threat": "Amazon Route 53 is a critical service; DNS hijacking or poisoning could redirect traffic to malicious sites.", "framework": "MITRE ATT&CK", "category": "Impact"},
            "vpc": {"threat": "VPC misconfiguration (e.g., overly permissive NACLs or security groups) can lead to unauthorized access between subnets.", "framework": "STRIDE", "category": "Information Disclosure"},
            "mainframe": {"threat": "On-prem mainframe may have legacy vulnerabilities or lack modern security monitoring.", "framework": "STRIDE", "category": "Spoofing"},
            "active-directory": {"threat": "On-prem Active Directory is a high-value target for credential theft and lateral movement.", "framework": "MITRE ATT&CK", "category": "Credential Access"},
            "end-user": {"threat": "End users are susceptible to phishing attacks, which can compromise credentials and provide initial access.", "framework": "MITRE ATT&CK", "category": "Initial Access"}
        }

        for component in architecture_data.get("components", []):
            component_type = component.get("type", "").lower()
            for keyword, threat_info in threat_definitions.items():
                if keyword in component_type:
                    threat = {
                        "component_id": component.get("id"),
                        "component_type": component.get("type"),
                        "threat": threat_info["threat"],
                        "framework": threat_info["framework"],
                        "category": threat_info["category"]
                    }
                    threats.append(threat)
        
        if not threats:
            print("No specific threats identified based on the current knowledge base.")
            
        return threats