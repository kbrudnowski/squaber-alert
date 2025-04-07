# 📈 Investment Alert App

A real-time alerting system for monitoring stock alerts using **Kafka**, **PySpark**, and **Telegram**.

---

## 🚀 Overview

This app scrapes live stock data, processes it using a streaming Spark job, and sends Telegram alerts when specific conditions are met.

### 🔧 Architecture

```text
[ Scraper (Kafka Producer) ] --> [ Kafka Topic: "stocks" ] --> [ PySpark Streaming App ] --> [ Telegram Alert ]
