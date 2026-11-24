# 1. Overview and Recommendation

This document collects the master's thesis ideas worth considering for the MSc in Data Science and Statistics (LM-82/LM-DATA, English-taught curriculum) at the University of Palermo, with graduation planned for 2027.

## 1.1 How the ideas were selected

Each idea was judged against five criteria:

1. **A real open question.** The question matters regardless of who studies it, and there is a visible gap or disagreement in the literature.
2. **Wide interest.** The results matter to people beyond one country or one company.
3. **Accessible data.** The core analysis can be done with free, public data. Company data is only ever an optional extra.
4. **Employability.** The skills involved are in demand in tech, fintech and finance roles.
5. **Fit with the programme.** The methods build on the curriculum's courses, and there are faculty members whose research matches.

## 1.2 Ranking

| Rank | Idea | Strongest point | Main risk |
|---|---|---|---|
| 1 | Does writing with ChatGPT help consumers win against banks? | Contested *Nature Human Behaviour* finding; free frozen dataset; AI, finance and public policy in one | The topic is attracting attention, so the thesis needs its own angle |
| 2 | Beyond Conversion: retention as the outcome of product experiments | Most directly employable (experimentation and survival analysis) | Public randomised data with retention outcomes does not exist, so it relies on semi-synthetic simulation |
| 3 | From dot-com to blockchain to AI: do markets learn from hype? | Memorable story; all data free | Defining "hype" carefully takes work |
| 4 | AI-washing: corporate AI talk vs. real AI activity | Very topical; free data | "AI talk" studies are multiplying |
| 5 | Central bank communication and markets | Established field with clear methods | Crowded literature |

**Recommendation.** Idea 1 is the most engaging and the most likely to become a publishable paper. Idea 2 is the safest choice for a career in product or growth data science. Both are written up as full proposals in Sections 3 and 4.

# 2. Programme Context

## 2.1 Relevant courses

The ideas draw on these courses from the Data Science and Statistics curriculum:

- Statistical Models and Machine Learning (Statistical Models; Statistical Machine Learning)
- Advanced Survival Analysis
- Data and Text Mining
- Big Data (Big Data Tools; Big Data Analytics)
- Stochastic Processes
- Non-Parametric Statistics
- Advanced Models for Complex Data
- Networks and High-Dimensional Data Analysis
- Performance Statistics and Statistical Models in Finance (including Statistical Models for Volatility in Finance)

## 2.2 Possible supervisors

Names come from the course listings. Research interests should be checked against each person's recent publications before contacting them.

| Area | Faculty | Relevant ideas |
|---|---|---|
| Text and data mining | Alessandro Albano | 1, 3, 4, 5 |
| Survival analysis | Massimo Attanasio | 2 |
| Non-parametric statistics, inference, segmented regression | Vito M. R. Muggeo | 1, 2 |
| Statistical machine learning, quantile regression | Gianluca Sottile | 1, 2 |
| Statistical models | Marcello Chiodi | 2 |
| Networks, statistically validated networks | Michele Tumminello, Andrea Simonetti | Other ideas (copy-trading, wash trading) |
| High-dimensional data, graphical models | Luigi Augugliaro | 4, other ideas |
| Stochastic and point processes | Giada Adelfio, Nicoletta D'Angelo | Other ideas (Hawkes processes) |
| Financial econometrics and volatility | Andrea Cipollini, Erasmo Vassallo | 3, 4, 5 |
| Economic statistics | Maria Francesca Cracolici | 5, other ideas |

# 3. Idea 1: Does Writing with ChatGPT Help Consumers Win Against Banks?

**Working title:** *AI as an Equaliser? Re-examining the Effect of LLM-Assisted Writing on Consumer Financial Complaints*

## 3.1 The story so far

- **February 2026, *Nature Human Behaviour*.** Shin, Kim and Shin analyse 1.13 million complaints to the US Consumer Financial Protection Bureau (CFPB), the agency that handles complaints against banks and lenders. They estimate that using an LLM to write a complaint raises the chance of obtaining relief by 6.9 percentage points (95% confidence interval 4.9 to 8.9). They argue LLMs act as an "equaliser" for disadvantaged consumers. Press coverage was wide.
- **October 2026, *Frontiers in Behavioral Economics*.** Cui finds only modest associations between how clear and coherent a complaint is and whether the company grants monetary relief.
- **November 2026, NYU Stern.** Vishal Singh publishes a reanalysis (a teaching case, not peer-reviewed). It uses an LLM-based detector checked against about 7,000 known chatbot rewrites. Comparing complaints to the same company, about the same product, in the same month, complaints flagged as AI-written receive monetary relief slightly *less* often. The gap is about the same size as the gap for complaints written before ChatGPT existed, which the detector wrongly flags. The data therefore cannot separate *using AI* from *writing in a formal style*.

There is a well-known claim, a credible challenge to it, and no resolution yet.

## 3.2 Why the two analyses disagree

| | Shin et al. (2026) | Singh (2026) |
|---|---|---|
| Detection of AI text | Commercial detector (Winston AI), 99% threshold | LLM-based detector checked against known chatbot rewrites |
| Outcome | Any relief (monetary or non-monetary) | Mainly monetary relief |
| Sample | Includes template letters from credit-repair firms | Excludes near-duplicates and templates |
| Separating cause from correlation | Instrumental variable: ZIP-code English proficiency and internet access | Comparisons within company, product and month; pre-ChatGPT placebo |
| Period | 2015 to 2024 | 2024 to mid-2025 |

Any of these differences could explain the different results. Sorting them out is the core of the thesis.

## 3.3 Research questions

1. **Reconciliation.** Which analysis choices drive the different answers? This uses a *multiverse analysis*: run every reasonable combination of choices and show how the estimate changes across them.
2. **Detector error.** What is the effect once the detector's mistakes (missed AI text and false alarms) are formally built into the statistical model?
3. **Does the advantage fade as everyone uses AI?** Singh estimates that more than half of 2026 narratives were AI-assisted. If polished text becomes the norm, companies may stop rewarding it. The archive runs to August 2026, so this can be tested directly. Neither of the two studies above addresses it.
4. **Fairness.** Older consumers use AI far less. Does AI narrow or widen the gaps in who gets relief?

## 3.4 Data

All of the data below is free:

- **CFPB Consumer Complaint Database.** The full dataset is a single CSV download (about 18 million complaints with product, issue, company, state, ZIP code, tags and the company's response).
- **CFPB narratives archive.** On 14 August 2026 the CFPB stopped publishing complaint texts in the live database and moved all previously published texts to its FOIA Electronic Reading Room. The archive covers December 2011 to August 2026, with several million narratives. Because it's frozen, results are fully reproducible.
- **US Census Bureau American Community Survey.** Characteristics of ZIP-code areas: age, income, education, share born abroad.
- **Cost of LLM scoring is low.** Singh reports scoring about 494,000 narratives for about USD 8.

## 3.5 Methods

| Step | Methods | Course link |
|---|---|---|
| Text processing | Near-duplicate and template detection (MinHash), AI-text detection, word-frequency estimation of the AI share (Liang et al., 2025) | Data and Text Mining; Big Data |
| Checking the detector | Rewriting pre-2022 complaints with several chatbots to build a known test set; measuring true- and false-positive rates | Statistical Machine Learning |
| Causal estimation | Instrumental variables, high-dimensional fixed effects, difference-in-differences, pre-ChatGPT placebo tests | Statistical Models |
| Correcting for detector error | Misclassification-corrected regression; prediction-powered inference | Statistical Inference |
| Robustness | Multiverse analysis; specification curves | Statistical Models |
| Scale | Processing millions of texts with DuckDB or Spark | Big Data |

## 3.6 Why it's worth doing

- **The question is universal:** whether AI gives ordinary people more power against institutions. The data is from the US, but the question applies everywhere.
- **A thesis that resolves a dispute over a top-journal paper is a strong candidate for publication.**
- **It covers finance (banks), tech (LLMs) and the public sector (a consumer-protection regulator).**
- **Employment value.** It combines causal inference, NLP and LLM evaluation, and large-scale data processing. Banks also need complaint analytics for compliance and regulatory work.

## 3.7 Risks

- **The topic is attracting attention.** Research questions 2 and 3 are what make the thesis original, so keep them central.
- **Every estimate remains an association unless the strategy for separating cause from correlation holds up.** That is also the most interesting part of the work.

**Possible supervisors:** Alessandro Albano (text mining), with Vito Muggeo or Gianluca Sottile (inference).

# 4. Idea 2: Beyond Conversion: Retention as the Outcome of Product Experiments

**Working title:** *Beyond Conversion: Measuring the Effect of Product Experiments on When Users Churn*

**Alternative title:** *Time-to-Event Outcomes in Online Controlled Experiments: Estimation, Sequential Monitoring and Heterogeneous Effects for Retention*

## 4.1 Motivation

Digital companies decide most product changes through A/B tests (online controlled experiments). Standard practice looks at short-term metrics such as conversion, click-through or first payment, measured over one to four weeks. For subscription businesses, though, what matters is **retention: how long a user stays and pays**.

This mismatch causes systematic errors:

- **Short-term wins can be long-term losses.** An aggressive paywall or discount can raise conversion while attracting users who churn faster. Hohnhold et al. (2015) at Google showed that short-term and long-term effects can point in opposite directions.
- **Retention is a time-to-event outcome with censoring.** When an experiment ends, many users are still subscribed. Treating "churned by day X" as a yes/no outcome throws away information and can bias the estimate.
- **The usual survival tools assume something false.** Hazard ratios and the log-rank test assume the treatment changes the churn rate by the same factor at every point in time (proportional hazards). Product changes often violate this, for example by raising early churn and lowering late churn (Hernán, 2010).
- **Peeking inflates false positives.** Checking results repeatedly before an experiment ends raises the false-positive rate (Johari et al., 2022). Methods that allow valid monitoring with censored data are rarely used in industry.

Biostatistics has mature tools for these problems from clinical trials, which are experiments with time-to-event outcomes. The online experimentation literature has mostly ignored them. **This thesis brings clinical-trial survival methodology to product experimentation and assesses where it works and where it fails.**

## 4.2 Research questions

1. **Short-term vs. long-term.** How often do short-term conversion metrics give the wrong sign or a misleading size for a treatment's effect on retention? Can a *surrogate index* (Athey et al., 2019), which combines several early signals into one predictor of the long-term outcome, predict the long-term effect early?
2. **Which effect measure and test?** Under non-proportional hazards, how do these compare in power, false-positive control and interpretability: the hazard ratio with the log-rank test, the Restricted Mean Survival Time (RMST, the average subscribed time within a fixed horizon), the difference in survival probability at a fixed time, and weighted log-rank tests?
3. **Monitoring during the experiment.** Can retention experiments be monitored continuously without inflating false positives? This compares group-sequential designs with alpha-spending (the clinical-trial approach) against anytime-valid confidence sequences.
4. **Who is affected, and how?** Which user segments does a change help or hurt? This uses causal survival forests, and separates voluntary cancellation from involuntary churn such as payment failure (competing risks).

## 4.3 Hypotheses

- **H1.** Conversion-focused interventions often show a short-term effect that disagrees with their effect on RMST, especially when the intervention changes *which users* convert.
- **H2.** Under realistic non-proportional hazards, RMST-based tests are as powerful as the log-rank test or more so, and are much easier to communicate ("users stay on average X more days in the first 90 days").
- **H3.** Sequential monitoring keeps the false-positive rate at its nominal level while reducing the average experiment duration.
- **H4.** Effects on churn vary substantially by acquisition channel, tenure and engagement. Separating voluntary from involuntary churn changes the conclusions.

## 4.4 Data

1. **Semi-synthetic simulation (main source).** The public **KKBox subscription churn dataset** (WSDM Cup 2018, Kaggle) contains millions of users with subscription transactions, cancellations and listening logs. Starting from real users and their real churn behaviour, users are randomly assigned to groups and known treatment effects are injected (proportional, crossing-hazards, delayed and segment-specific). This is called a plasmode simulation. Because the true effect is known, every method can be compared fairly.
2. **Real experiment metadata.** The **ASOS Digital Experiments Dataset** (Liu et al., 2021) sets realistic effect sizes and is used to study sequential monitoring on real experiment paths.
3. **Industry data (optional).** Anonymised experiment data from a subscription company, obtained through the curriculum's internship or statistical consulting credits under a formal data agreement. The thesis does not depend on it.

## 4.5 Methodology

| Component | Methods | Course link |
|---|---|---|
| Descriptive survival analysis | Kaplan-Meier curves, cumulative incidence functions | Advanced Survival Analysis |
| Effect measures | Hazard ratio from the Cox model, RMST difference, survival difference at fixed times, weighted log-rank tests | Advanced Survival Analysis |
| Competing risks | Cause-specific hazards; the Fine-Gray model | Advanced Survival Analysis |
| Long-term prediction | Surrogate index; joint models of engagement over time and churn | Statistical Models; Advanced Models for Complex Data |
| Sequential monitoring | Group-sequential designs (O'Brien-Fleming, Lan-DeMets); anytime-valid confidence sequences | Statistical Inference; Stochastic Processes |
| Heterogeneous effects | Causal survival forests; random survival forests | Statistical Machine Learning |
| Variance reduction | Adjustment with pre-experiment covariates (CUPED) | Statistical Models |
| Scale | Tens of millions of transaction rows with Spark, Databricks or BigQuery | Big Data |

Methods are evaluated on statistical power, false-positive rate, bias and coverage of the estimated effect, average experiment duration, and decision accuracy (how often a method leads to the right ship or don't-ship decision).

## 4.6 Expected contributions

1. A benchmark of statistical methods for retention experiments under realistic conditions.
2. Evidence on how often short-term metrics mislead about long-term retention, and whether early surrogates help.
3. A practical decision guide for analysts: which measure, which test, how long to run, and when it is safe to stop.
4. An open-source R or Python toolkit with reproducible code.

## 4.7 Work plan

| Phase | Activities |
|---|---|
| 1. Literature and setup | Review of clinical-trial survival methods and online experimentation; KKBox data cleaning and Spark pipeline |
| 2. Simulation framework | Plasmode design and treatment-effect scenarios |
| 3. Research questions 1 and 2 | Short- vs. long-term disagreement; comparison of effect measures |
| 4. Research questions 3 and 4 | Sequential monitoring; heterogeneous effects and competing risks |
| 5. Industry case study (optional) | Application to real experiment data |
| 6. Writing | Thesis, toolkit documentation, defence preparation |

If the supervisor suggests narrowing the scope, the natural core is research questions 2 and 3.

**Possible supervisors:** Massimo Attanasio (survival analysis), with Vito Muggeo or Gianluca Sottile.

# 5. Idea 3: From Dot-Com to Blockchain to AI: Do Markets Learn from Hype?

**Working title:** *Three Hype Waves: Corporate Buzzwords, Market Reactions and Serial Hypers, 1998 to 2026*

## 5.1 The problem

Every technology wave produces companies that rebrand themselves around the buzzword:

- **Dot-com.** Cooper, Dimitrov and Rau (2001) found that firms adding ".com" to their names in 1998-1999 earned large abnormal returns.
- **Blockchain.** In December 2017, Long Island Iced Tea Corp. renamed itself Long Blockchain and its stock jumped by roughly 200% in a day. The SEC later brought insider-trading charges connected to it. Cheng et al. (2019) studied speculative blockchain 8-K disclosures.
- **AI.** Since 2023, mentions of AI in company filings have exploded.

## 5.2 Research questions

1. Did markets reward buzzword disclosures less in each new wave, which would mean investors learn?
2. Are the *same companies* hyping successive waves ("serial hypers")? Do they share characteristics: size, profitability, insider selling around announcements?
3. Do hypers underperform in the long run compared with similar firms?
4. Can text mining separate substantive announcements from cosmetic ones, and do markets price that difference?

## 5.3 Data

All free:
- SEC EDGAR full-text filings (8-K, 10-K) back to the late 1990s
- Company name-change histories from EDGAR
- Stock prices from Yahoo Finance (`yfinance`), or WRDS/CRSP if available through the university

## 5.4 Methods

- Keyword and embedding-based detection of buzzword disclosures
- Event studies (abnormal returns and trading volume) around announcements
- Matched-sample long-run performance analysis
- Classification of each announcement as substantive or cosmetic, checked against a hand-labelled sample

**Possible supervisors:** Alessandro Albano (text mining), with Andrea Cipollini or Erasmo Vassallo (finance).

# 6. Idea 4: AI-Washing: Corporate AI Talk vs. Real AI Activity

**Working title:** *Talking AI: Measuring the Gap Between Corporate AI Rhetoric and Real AI Activity, and How Markets Price It*

## 6.1 The problem

Since ChatGPT launched in November 2022, mentions of AI in company reports have exploded. Some companies are genuinely building AI; others use the word to look innovative ("AI-washing"). In March 2024 the SEC fined two investment advisers, Delphia and Global Predictions, for misleading AI claims. AI-washing is now a regulatory issue.

## 6.2 Research questions

1. **Measurement.** Can AI mentions in annual reports be reliably separated into substantive claims (specific products, deployments, numbers) and vague ones? How well do LLMs do this compared with simpler text-mining methods?
2. **Talk vs. substance.** Do companies with more AI talk show more real AI activity, measured by AI patents and R&D spending?
3. **Market reaction.** Do stock prices reward vague talk as much as substantive talk, and does vague talk predict worse performance later?
4. **Regulation.** Did vague AI language decline after the 2024 SEC enforcement actions? This is tested with difference-in-differences.

## 6.3 Data

All free:
- SEC EDGAR full-text 10-K filings, plus the XBRL "company facts" API for R&D and revenues
- USPTO Artificial Intelligence Patent Dataset (Giczy, Pairolero and Toole, 2022) and PatentsView
- Stock prices from Yahoo Finance, or WRDS if available

## 6.4 Methods

- Classification of AI passages as substantive or vague, comparing an LLM, a fine-tuned transformer and a TF-IDF baseline against about 1,000 hand-labelled passages
- Topic models and embeddings to describe *what* companies say about AI
- Panel regressions linking AI talk to patents and R&D
- Event studies around filings
- Difference-in-differences around the SEC actions

**Possible supervisors:** Alessandro Albano, with Andrea Cipollini or Erasmo Vassallo.

**Note:** Ideas 3 and 4 combine naturally. The AI wave becomes the final chapter of the hype-cycle study.

# 7. Idea 5: Central Bank Communication and Markets

**Working title:** *Words That Move Markets: Measuring Central Bank Tone with LLMs*

## 7.1 The problem and questions

Markets react not only to central bank decisions but to how central banks communicate. The questions:

1. Do LLM-based measures of tone and uncertainty in Federal Reserve, ECB and Bank of England communication predict market reactions better than traditional dictionary methods?
2. Does communication from one central bank spill over to other countries' markets?

An Italy-focused variant studies whether ECB tone, and text-measured Italian political tension, move the BTP-Bund spread (the extra interest Italy pays compared with Germany), including before and after the ECB's Transmission Protection Instrument (2022).

## 7.2 Data

All free:
- Fed statements, minutes and press conference transcripts (federalreserve.gov)
- ECB press conferences and the ECB speeches dataset
- Bank of England publications
- Daily yields and volatility indices from FRED

## 7.3 Methods

- Dictionary methods (Loughran-McDonald), topic models and LLM-based tone scores
- Event studies
- Volatility (GARCH-type) models with text-based explanatory variables

**Possible supervisors:** Andrea Cipollini or Erasmo Vassallo, with Alessandro Albano.

**Main risk:** The literature is crowded, so a clear methodological angle is essential (for example, a rigorous validation of LLM tone measures).

# 8. Other Ideas Considered

These ideas are less developed but remain viable. Each comes with its main data source and risk.

## 8.1 Herding in social trading networks

Do networks of retail investors who trade together amplify herding and volatility, especially around meme-stock and crypto events? Statistically validated networks (Tumminello et al., 2011) identify investor links that are not due to chance.
- **Data:** Archived Robinhood popularity data, Reddit r/wallstreetbets, Stocktwits
- **Supervisors:** Michele Tumminello, Luigi Augugliaro
- **Risk:** Data access for individual-level trades

## 8.2 Social media hype and trading as self-exciting processes

Do social media posts drive bursts of retail trading, or the reverse? Bivariate Hawkes processes measure which stream excites the other and how fast the effect decays.
- **Data:** Public crypto exchange trades (for example Binance), Reddit posts
- **Supervisors:** Giada Adelfio, Nicoletta D'Angelo
- **Risk:** Mathematically demanding; well suited to a PhD path

## 8.3 Detecting wash trading on blockchains

Can network-based statistical tests find coordinated fake trading in NFT or token markets, and how much reported volume is fake (Cong et al., 2023)?
- **Data:** Public Ethereum data (Google BigQuery public datasets) or Polkadot/Subscan APIs
- **Supervisors:** Michele Tumminello, Andrea Simonetti
- **Risk:** Large data volumes

## 8.4 The digital gender gap in finance

As banking moves to mobile, do women and rural users fall further behind? Uses multilevel models, quantile regression and decomposition methods (Oaxaca-Blinder and its quantile version).
- **Data:** World Bank Global Findex microdata; ECB Household Finance and Consumption Survey
- **Supervisors:** Mariangela Sciandra, Maria Francesca Cracolici, Gianluca Sottile
- **Risk:** Low; clean data, but less novel methodologically

## 8.5 Generative AI and the demand for data skills

Using job postings from before and after ChatGPT, which skills are rising or falling in data analyst and data scientist ads, and are entry-level roles shrinking? Skills are extracted from ad text and changes are analysed with difference-in-differences.
- **Data:** Eurostat online job advertisement statistics; public LinkedIn job-posting datasets on Kaggle; Indeed Hiring Lab data
- **Supervisors:** Maria Francesca Cracolici, with Alessandro Albano
- **Risk:** Raw ad text over a long period is hard to obtain for free

## 8.6 Corruption risk in public procurement

Does the *text* of tender descriptions add information on corruption risk beyond standard red flags such as single bidders and short deadlines (Fazekas and Kocsis, 2020)?
- **Data:** Italian ANAC open data; EU Tenders Electronic Daily (TED)
- **Supervisors:** Alessandro Albano, with Davide Piacentino or Ornella Giambalvo
- **Risk:** Ground truth for corruption is indirect

## 8.7 Young-graduate emigration from Georgia and Sicily

What predicts who leaves and when, and does skills education retain people or accelerate departure? Uses event-history models.
- **Data:** ISTAT, AlmaLaurea, Geostat, Eurostat
- **Supervisor:** Massimo Attanasio
- **Risk:** Georgian microdata is harder to obtain

# 9. Next Steps

1. **Shortlist two ideas** and read two or three recent papers by each possible supervisor.
2. **Write to supervisors early** with a one-paragraph summary, the research questions and the dataset. Concrete data and questions get better responses.
3. **Verify every reference** in Google Scholar before quoting it in a proposal.
4. **Download the key datasets early** and check their size, fields and terms of use.
5. **Check for written permission** before using any data from a former employer. Employment contracts usually restrict this.
6. **Consider combining the thesis with the 6-credit internship or consulting activity,** so the two support each other.

# 10. References

- Acemoglu, D., Autor, D., Hazell, J., & Restrepo, P. (2022). Artificial intelligence and jobs: Evidence from online vacancies. *Journal of Labor Economics*.
- Angelopoulos, A. N., Bates, S., Fannjiang, C., Jordan, M. I., & Zrnic, T. (2023). Prediction-powered inference. *Science*.
- Athey, S., Chetty, R., Imbens, G., & Kang, H. (2019). The surrogate index: Combining short-term proxies to estimate long-term treatment effects more rapidly and precisely. *NBER Working Paper 26463*.
- Babina, T., Fedyk, A., He, A., & Hodson, J. (2024). Artificial intelligence, firm growth, and product innovation. *Journal of Financial Economics*.
- Cheng, S. F., De Franco, G., Jiang, H., & Lin, P. (2019). Riding the blockchain mania: Public firms' speculative 8-K disclosures. *Management Science*.
- Cong, L. W., Li, X., Tang, K., & Yang, Y. (2023). Crypto wash trading. *Management Science*.
- Cooper, M. J., Dimitrov, O., & Rau, P. R. (2001). A Rose.com by any other name. *Journal of Finance*.
- Cui, F. (2026). Predicted clarity, coherence, and monetary relief in 94,335 Consumer Financial Protection Bureau complaints. *Frontiers in Behavioral Economics*.
- Cui, Y., Kosorok, M. R., Sverdrup, E., Wager, S., & Zhu, R. (2023). Estimating heterogeneous treatment effects with right-censored data via causal survival forests. *Journal of the Royal Statistical Society: Series B*.
- Deng, A., Xu, Y., Kohavi, R., & Walker, T. (2013). Improving the sensitivity of online controlled experiments by utilizing pre-experiment data. *WSDM*.
- Fazekas, M., & Kocsis, G. (2020). Uncovering high-level corruption: Cross-national objective corruption risk indicators using public procurement data. *British Journal of Political Science*.
- Fine, J. P., & Gray, R. J. (1999). A proportional hazards model for the subdistribution of a competing risk. *Journal of the American Statistical Association*.
- Gentzkow, M., Kelly, B., & Taddy, M. (2019). Text as data. *Journal of Economic Literature*.
- Giczy, A. V., Pairolero, N. A., & Toole, A. A. (2022). Identifying artificial intelligence (AI) invention: A novel AI patent dataset. *Journal of Technology Transfer*.
- Hansen, S., McMahon, M., & Prat, A. (2018). Transparency and deliberation within the FOMC: A computational linguistics approach. *Quarterly Journal of Economics*.
- Hassan, T. A., Hollander, S., van Lent, L., & Tahoun, A. (2019). Firm-level political risk: Measurement and effects. *Quarterly Journal of Economics*.
- Hernán, M. A. (2010). The hazards of hazard ratios. *Epidemiology*.
- Hershbein, B., & Kahn, L. B. (2018). Do recessions accelerate routine-biased technological change? Evidence from vacancy postings. *American Economic Review*.
- Hohnhold, H., O'Brien, D., & Tang, D. (2015). Focusing on the long-term: It's good for users and business. *KDD*.
- Howard, S. R., Ramdas, A., McAuliffe, J., & Sekhon, J. (2021). Time-uniform, nonparametric, nonasymptotic confidence sequences. *Annals of Statistics*.
- Ishwaran, H., Kogalur, U. B., Blackstone, E. H., & Lauer, M. S. (2008). Random survival forests. *Annals of Applied Statistics*.
- Jennison, C., & Turnbull, B. W. (2000). *Group Sequential Methods with Applications to Clinical Trials*. Chapman & Hall/CRC.
- Johari, R., Koomen, P., Pekelis, L., & Walsh, D. (2022). Always valid inference: Continuous monitoring of A/B tests. *Operations Research*.
- Kohavi, R., Tang, D., & Xu, Y. (2020). *Trustworthy Online Controlled Experiments*. Cambridge University Press.
- Liang, W., Zhang, Y., Codreanu, M., Wang, J., Cao, H., & Zou, J. (2025). The widespread adoption of large language model-assisted writing across society. *Patterns*.
- Liu, C. H. B., Cardoso, Â., Couturier, P., & McCoy, E. J. (2021). Datasets for online controlled experiments. *NeurIPS Datasets and Benchmarks Track*.
- Loughran, T., & McDonald, B. (2011). When is a liability not a liability? Textual analysis, dictionaries, and 10-Ks. *Journal of Finance*.
- Rizopoulos, D. (2012). *Joint Models for Longitudinal and Time-to-Event Data*. CRC Press.
- Royston, P., & Parmar, M. K. B. (2013). Restricted mean survival time: An alternative to the hazard ratio for the design and analysis of randomized trials with a time-to-event outcome. *BMC Medical Research Methodology*.
- Shin, M., Kim, J., & Shin, J. (2026). The adoption and efficacy of large language models in US consumer financial complaints. *Nature Human Behaviour*, 10(4), 669-680.
- Simonsohn, U., Simmons, J. P., & Nelson, L. D. (2020). Specification curve analysis. *Nature Human Behaviour*.
- Singh, V. (2026). *How much consumer complaint text is written with AI?* Teaching case, NYU Stern School of Business.
- Tumminello, M., Miccichè, S., Lillo, F., Piilo, J., & Mantegna, R. N. (2011). Statistically validated networks in bipartite complex systems. *PLoS ONE*.
- US Securities and Exchange Commission (2024). SEC charges two investment advisers with making false and misleading statements about their use of artificial intelligence. Press release 2024-36.
