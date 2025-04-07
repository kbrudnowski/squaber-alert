# 📈 Investment Alert App

A real-time alerting system for monitoring stock alerts using **Kafka**, **PySpark**, and **Telegram**.

---

## 🚀 Overview

This app scrapes live stock data, processes it using a streaming Spark job, and sends Telegram alerts when specific conditions are met.

### 🔧 Architecture

```text
[ Scraper (Kafka Producer) ] --> [ Kafka Topic: "stocks" ] --> [ PySpark Streaming App ] --> [ Telegram Alert ]

---

## ⚙️ Components

### 1. Kafka Producer (Python)
- Scrapes stock data using 
- Publishes price info to Kafka topic `"stocks"`

### 2. Spark Streaming Job (PySpark)
- Reads from Kafka topic in real-time
- Applies condition logic (e.g. alert if `price is lower than avg and financial condition is good`)
- Triggers Telegram alert

### 3. Telegram Bot
- Sends alert messages to your Telegram chat
- Easily configurable with your own bot token and chat ID

---

## ✅ Requirements

- Python 3.8+
- Docker & Docker Compose
- Apache Spark (or use Dockerized version)
- Kafka (Docker recommended)
- Telegram bot via [@BotFather](https://t.me/BotFather)

