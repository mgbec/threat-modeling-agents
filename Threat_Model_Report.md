# Threat Model Report

## Executive Summary

| Risk Level | Count |
|------------|-------|
| Critical | 1 |
| High | 8 |
| Medium | 1 |
| Low | 1 |

## Detailed Findings

### Critical - On-prem Active Directory is a high-value target for credential theft and lateral movement.
- **Component ID**: `18`
- **Component Type**: `on-prem-active-directory`
- **Assessed Impact**: High
- **Assessed Likelihood**: High
- **Threat Framework**: MITRE ATT&CK (Credential Access)

### High - Auto Scaling group misconfiguration could lead to resource exhaustion or insufficient capacity during an attack.
- **Component ID**: `1`
- **Component Type**: `aws-auto-scaling-group`
- **Assessed Impact**: Medium
- **Assessed Likelihood**: High
- **Threat Framework**: STRIDE (Denial of Service)

### High - Auto Scaling group misconfiguration could lead to resource exhaustion or insufficient capacity during an attack.
- **Component ID**: `2`
- **Component Type**: `aws-auto-scaling-group`
- **Assessed Impact**: Medium
- **Assessed Likelihood**: High
- **Threat Framework**: STRIDE (Denial of Service)

### High - Application Load Balancer may have misconfigured listeners or security groups, exposing backend services.
- **Component ID**: `3`
- **Component Type**: `aws-application-load-balancer`
- **Assessed Impact**: High
- **Assessed Likelihood**: Medium
- **Threat Framework**: MITRE ATT&CK (Initial Access)

### High - Internet Gateway is a potential single point of failure and a primary target for DDoS attacks.
- **Component ID**: `4`
- **Component Type**: `aws-internet-gateway`
- **Assessed Impact**: Medium
- **Assessed Likelihood**: High
- **Threat Framework**: STRIDE (Denial of Service)

### High - Amazon Route 53 is a critical service; DNS hijacking or poisoning could redirect traffic to malicious sites.
- **Component ID**: `5`
- **Component Type**: `aws-route53`
- **Assessed Impact**: High
- **Assessed Likelihood**: Low
- **Threat Framework**: MITRE ATT&CK (Impact)

### High - Application Load Balancer may have misconfigured listeners or security groups, exposing backend services.
- **Component ID**: `6`
- **Component Type**: `aws-application-load-balancer`
- **Assessed Impact**: High
- **Assessed Likelihood**: Medium
- **Threat Framework**: MITRE ATT&CK (Initial Access)

### High - Internet Gateway is a potential single point of failure and a primary target for DDoS attacks.
- **Component ID**: `7`
- **Component Type**: `aws-internet-gateway`
- **Assessed Impact**: Medium
- **Assessed Likelihood**: High
- **Threat Framework**: STRIDE (Denial of Service)

### High - End users are susceptible to phishing attacks, which can compromise credentials and provide initial access.
- **Component ID**: `22`
- **Component Type**: `end-user`
- **Assessed Impact**: High
- **Assessed Likelihood**: Medium
- **Threat Framework**: MITRE ATT&CK (Initial Access)

### Medium - VPC misconfiguration (e.g., overly permissive NACLs or security groups) can lead to unauthorized access between subnets.
- **Component ID**: `8`
- **Component Type**: `aws-vpc`
- **Assessed Impact**: Medium
- **Assessed Likelihood**: Medium
- **Threat Framework**: STRIDE (Information Disclosure)

### Low - On-prem mainframe may have legacy vulnerabilities or lack modern security monitoring.
- **Component ID**: `17`
- **Component Type**: `on-prem-mainframe`
- **Assessed Impact**: Low
- **Assessed Likelihood**: Medium
- **Threat Framework**: STRIDE (Spoofing)

