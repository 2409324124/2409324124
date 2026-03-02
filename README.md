# 👋 你好，我是东云

**`独立研究者 | 硬件实践者 | 深度学习探索者`**

我是一名从**名为社会的规劝**走来的跨学科探索者。我深信，**深度学习的未来不在于创造更孤立的智能，而在于构建更能理解人、关怀人的技术，实现每个人的成长**。

> “助人自助。”—— 将社会工作中的这句信条，带入我对电子信息技术与复杂世界的探索中。

---
## 最新项目：从零实现 Seq2Seq + Bahdanau Attention 神经机器翻译 (2026.2 更新)

**项目仓库**：https://github.com/2409324124/seq2seq-nmt-from-scratch

纯 PyTorch 从头复刻经典 Seq2Seq 框架（Sutskever 2014 核心技巧 + Bahdanau Attention），在 Multi30k 数据集（德语 → 英语）上达到 **BLEU 56.3**（sacreBLEU，test set）——远超大多数教程水平。

### 模型架构概览
<p align="center">
  <img src="https://github.com/2409324124/seq2seq-nmt-from-scratch/raw/main/model_architecture_bahdanau_lstm.png" 
       alt="Bahdanau Attention + LSTM Seq2Seq 架构图" width="700"/>
  <br>
  <em>编码器 → 加性注意力 → 解码器（支持源句子反转 + input feeding）</em>
</p>


### 实时交互翻译 Demo（Gradio 界面）

<p align="center">
  <a href="https://huggingface.co/spaces/xu2409324124/lstm-translator" target="_blank">
    <img src="https://img.shields.io/badge/🚀_立即体验实时翻译-FF4D4D?style=for-the-badge&logo=huggingface&logoColor=white&labelColor=000000" alt="Try Live Demo"/>
  </a>
</p>

<p align="center">
  <em>支持德语 → 英语实时翻译，基于我们从零实现的 LSTM + Bahdanau Attention 模型</em>
</p>

### 训练过程可视化
<p align="center">
  <img src="https://github.com/2409324124/seq2seq-nmt-from-scratch/raw/main/loss_curve_lstm.png" 
       alt="训练 & 验证 Loss 曲线" width="600"/>
  <br>
  <em>蓝色：训练 Loss　　红色：验证 Loss　　最佳验证 Loss ≈4.34（早停）</em>
</p>

### 注意力机制解释性示例
<p align="center">
  <img src="https://github.com/2409324124/seq2seq-nmt-from-scratch/raw/main/attention_heatmap_example.jpeg" 
       alt="注意力热图示例" width="600"/>
  <br>
  <em>横轴：德语源句（已反转）　　纵轴：生成的英语　　颜色深度 = 关注权重</em>
</p>

### 项目亮点 & 成果
- LSTM + Bahdanau Attention 全链路实现（hidden=256~512，dropout=0.4，label smoothing）
- 动态 teacher forcing + 梯度裁剪 + AdamW + 早停
- Beam Search 解码 & sacreBLEU 评估
- 实时 Gradio 翻译界面（已部署）：https://huggingface.co/spaces/xu2409324124/lstm-translator
- 从零基础自学里程碑：MNIST CNN → GRU Seq2Seq → 这个高性能 NMT 项目

欢迎点进仓库 star / fork / 试用 demo！也欢迎讨论优化方向（bidirectional、multi-head attention、pretrained embedding）或跨领域合作（AI + 心理学、社会学）。

更多细节 & 运行指南 → [前往项目仓库](https://github.com/2409324124/seq2seq-nmt-from-scratch)
--- 

## 🧠 我的背景故事：从人文关怀到技术实现

我的职业路径塑造了我独特的视角：

*   **🏛️ 社会工作者**：在社区和社工服务机构一线的经历，让我深入理解了人类行为于社会环境的复杂性、社会系统的运作以及**共情与沟通**的核心价值。
*   **🔧 硬件工程师**：在长城电子的经历锤炼了我的**精密操作、流程严谨性与质量第一**的思维。我习惯于在明确的规范下解决问题，并将这种结构化思维带入代码世界。
*   **🤖 深度学习研究者**：现在，我正系统学习深度学习，目标是将上述所有经验融合，用算法模型定量地研究心理学问题，例如**情绪识别、社会行为模式分析或心理状态评估**。

于混沌的暮色中观测，在涌现的秩序里连接。

---

## 🛠️ 技术栈与工具箱

我正在积极构建我的技术栈，每一步都力求稳固：

<p align="center">
  <!-- 核心编程与深度学习 -->
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="Hugging Face"/>
  <img src="https://img.shields.io/badge/Gradio-3E8EFB?style=for-the-badge&logo=gradio&logoColor=white" alt="Gradio"/>
  <br><br>

  <!-- 现代 AI Agent 工具 -->
  <img src="https://img.shields.io/badge/Google%20Gemini-8E75FF?style=for-the-badge&logo=google&logoColor=white" alt="Google Gemini"/>
  <img src="https://img.shields.io/badge/Coze-FF6A00?style=for-the-badge&logo=coze&logoColor=white" alt="Coze"/>
  <img src="https://img.shields.io/badge/AI%20Agent-FF4D4D?style=for-the-badge&logo=robot&logoColor=white" alt="AI Agent"/>
  <br><br>

  <!-- 数据科学与研究工具 -->
  <img src="https://img.shields.io/badge/NumPy-4DABCF?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter"/>
  <img src="https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white" alt="VS Code"/>
  <br><br>

  <!-- Adobe 创意工具 -->
  <img src="https://img.shields.io/badge/adobe%20photoshop-%2331A8FF.svg?style=for-the-badge&logo=adobe%20photoshop&logoColor=white" alt="Photoshop"/>
  <img src="https://img.shields.io/badge/Adobe%20Premiere%20Pro-9999FF.svg?style=for-the-badge&logo=Adobe%20Premiere%20Pro&logoColor=white" alt="Premiere Pro"/>
  <img src="https://img.shields.io/badge/Adobe%20After%20Effects-9999FF.svg?style=for-the-badge&logo=Adobe%20After%20Effects&logoColor=white" alt="After Effects"/>
  <img src="https://img.shields.io/badge/adobe%20illustrator-%23FF9A00.svg?style=for-the-badge&logo=adobe%20illustrator&logoColor=white" alt="Illustrator"/>
  <br><br>

  <!-- 本地推理与传统研究工具 -->
  <img src="https://img.shields.io/badge/ollama-%23000000.svg?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama"/>
  <img src="https://img.shields.io/badge/NVivo-003366?style=for-the-badge&logoColor=white" alt="NVivo"/>
  <img src="https://img.shields.io/badge/SPSS-054ADA?style=for-the-badge&logo=ibm&logoColor=white" alt="SPSS"/>
  <img src="https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white" alt="Excel"/>
</p>
---

| 类别              | 正在学习/使用 |
|-------------------|---------------|
| **💻 编程语言**   | Python（主要研究语言） |
| **🧠 深度学习框架** | PyTorch（灵活动态图首选） + Ollama（本地大模型推理） |
| **🎨 创意/视频工具** | Photoshop, Premiere Pro, After Effects, Illustrator |
| **📊 研究与数据分析** | NVivo（定性编码）、SPSS（统计）、Excel（基础建模） |
| **🎯 关注领域**   | NLP、可解释AI(XAI)、智能精神健康干预、深度学习 |

---

## 📂 项目与探索
这里记录我“从零到一”的学习与实践历程，从基础笔记到完整 NLP 项目，逐步构建系统能力：

| 项目 | 描述 | 状态 |
|------|------|------|
| **🔬 [计算心理学](https://github.com/2409324124/Computational-Psychology)** | 系统梳理 AI 与心理学研究的经典与前沿论文，探索技术如何服务人类心理健康。 | **持续更新** |
| **🧠 [Seq2Seq 神经机器翻译从零实现](https://github.com/2409324124/seq2seq-nmt-from-scratch)** | 纯 PyTorch 从头复现 LSTM + Attention 的 Seq2Seq 模型（Multi30k 德→英翻译），包含完整训练、BLEU 评估、Loss/Attention 可视化、Gradio 交互 demo（已部署 Hugging Face）。最新里程碑：BLEU 56.3，Gradio 实时翻译体验。 | **最新完成 & 持续优化** |

---

## 🌱 当前聚焦

我正在全力探索新一代 AI 开发范式与智能体工程：

<p align="center">
  <img src="https://img.shields.io/badge/AI%20Agent-FF4D4D?style=for-the-badge&logo=robot&logoColor=white" alt="AI Agent"/>
  <img src="https://img.shields.io/badge/Antigravity%20(Vibe%20Coding)-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Google Antigravity"/>
  <img src="https://img.shields.io/badge/Coze-FF6A00?style=for-the-badge&logo=coze&logoColor=white" alt="Coze"/>
</p>

- **🤖 AI Agent 系统**：构建自主规划、工具调用、多代理协作的智能体应用
- **🚀 Google Antigravity（反重力）**：深度使用 Google 最新发布的 Agent-first IDE，搭配 Gemini 3 Pro 进行「Vibe Coding」（氛围编码），直接把想法变成完整可运行的全栈应用
- **🌟 Coze 平台**：在字节跳动 Coze 上快速搭建多模态 Agent 与复杂工作流，支持无代码/低代码高效开发与跨平台部署

这些前沿工具将与我的**计算心理学 + 深度学习 + 人文关怀**背景深度融合，目标是做出真正能理解人、帮助人的智能应用。 

## 📮 与我连接

我深知跨学科之路需要与更多元的头脑交流。欢迎交流任何想法：

- **💌 邮箱**：xu2409324124@gmail.com  
- **🐱 GitHub**：[@2409324124](https://github.com/2409324124) —— 你正在访问的地方  
- **📝 技术博客/笔记站**：（待补充）

> **✨ 协作邀请**：如果你也对**深度学习、心理学、神经科学或任何致力于理解人类的技术**感兴趣，或者你正在从事相关研究，我非常期待与你对话。

---
*这份简介本身也是一个持续学习的项目，它会随着我的认知迭代而不断演化。*
