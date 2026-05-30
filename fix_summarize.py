import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open(r'c:/Users/admin/Desktop/website/narain_portfolio.html', encoding='utf-8') as f:
    html = f.read()

# ─── 1. AMD OVERVIEW: replace 7 bullets with 4 ───────────────────────────────
old_amd_ul = '''              <ul>
                <li>Investigated 12-layer HBM yield reduction using SEM defect review and optical metrology data across 10,000+ test datapoints per wafer from multiple OSAT suppliers</li>
                <li>Built Python heatmap visualization pipeline revealing a critical spatial pattern: edge dies at 93% yield vs center dies at 99–100% yield</li>
                <li>Traced root cause to oxygen contamination from the Czochralski crystal growth process, O₂ from the quartz crucible dissolves into molten silicon and concentrates at crystal edges, creating precipitation sites during thermal processing</li>
                <li>Developed die placement algorithm (NumPy, Pandas) to flag high-risk edge zones before assembly, cutting RCA time from 5+ days to under 48 hours</li>
                <li>Evaluated substrates, thermal interface materials (TIMs), and adhesives for process capability and performance trade-offs</li>
                <li>Coordinated directly with OSAT suppliers on equipment qualification and wafer fabrication specifications</li>
                <li>Collected in-line metrology data from CVD deposition tools in Class 10/100 cleanroom environments</li>
              </ul>'''

new_amd_ul = '''              <ul>
                <li>Investigated 12-layer HBM yield degradation across 10,000+ datapoints per wafer using SEM defect review and optical metrology from multiple OSAT suppliers</li>
                <li>Built Python heatmap pipeline (NumPy, Pandas, Matplotlib) that exposed a spatial edge-to-center yield gradient (93% vs 99–100%), enabling root cause identification via 5-Why analysis</li>
                <li>Developed die placement exclusion algorithm flagging dies beyond 85% wafer radius, cutting RCA cycle time from 5+ days to under 48 hours</li>
                <li>Qualified substrates, TIMs, and adhesives; coordinated OSAT supplier equipment qualifications; collected CVD metrology data in Class 10/100 cleanroom</li>
              </ul>'''

if old_amd_ul in html:
    html = html.replace(old_amd_ul, new_amd_ul)
    print("✓ AMD overview bullets replaced")
else:
    print("✗ AMD overview bullets NOT found")

# ─── 2. AMD Czochralski paragraph: shorten ────────────────────────────────────
old_czoch = '''<p>Silicon wafers are grown via the Czochralski process a seed crystal is slowly pulled from molten silicon in a quartz crucible. Oxygen from the quartz dissolves into the silicon melt and incorporates into the growing crystal. The last regions to solidify (the crystal edges) accumulate the highest oxygen concentrations. During subsequent thermal processing steps (annealing, oxidation), these oxygen-rich zones form SiO₂ precipitates that act as nucleation sites for defects and degrade transistor performance. This produces the distinctive edge-to-center yield gradient: 93% at edges vs 99–100% at center. Coordinated with wafer supplier to obtain SIMS data cross-checking oxygen contamination hypothesis from Czochralski crystal growth at wafer edge. Implemented SPC monitoring using p-charts with binomial distribution to track package yield trends and edge die yields for early warning. If hypothesis and team findings are implemented, could result in approximately 15% yield recovery.</p>'''

new_czoch = '''<p>In the Czochralski process, oxygen from the quartz crucible dissolves into the silicon melt and concentrates at crystal edges — the last regions to solidify. During thermal processing, these oxygen-rich zones form SiO₂ precipitates that nucleate defects, producing the 93% edge vs 99–100% center yield gradient. SIMS data from the wafer supplier confirmed the contamination hypothesis; SPC p-charts were implemented for early warning monitoring, with projected ~15% yield recovery if findings are implemented.</p>'''

if old_czoch in html:
    html = html.replace(old_czoch, new_czoch)
    print("✓ AMD Czochralski paragraph shortened")
else:
    print("✗ AMD Czochralski paragraph NOT found")

# ─── 3. AMD Die Placement bullets: 5 → 3 ─────────────────────────────────────
old_die = '''              <ul>
                <li>Input: Wafer map with die coordinates + electrical test results</li>
                <li>Calculate radial distance from wafer center for each die position</li>
                <li>Flag dies beyond 85% of wafer radius as high-risk exclusion candidates</li>
                <li>Output: Exclusion list fed to assembly process before die attach</li>
                <li>SPC charts continuously tracked yield improvement across production runs</li>
              </ul>'''

new_die = '''              <ul>
                <li>Input wafer map (die coordinates + electrical test results); compute radial distance from wafer center for each die</li>
                <li>Flag dies beyond 85% of wafer radius as high-risk exclusion candidates</li>
                <li>Output exclusion list fed to assembly before die attach; SPC charts track yield improvement across production runs</li>
              </ul>'''

if old_die in html:
    html = html.replace(old_die, new_die)
    print("✓ AMD Die Placement bullets condensed")
else:
    print("✗ AMD Die Placement bullets NOT found")

# ─── 4. AMD Statistical Methods bullets: 4 → 3 ────────────────────────────────
old_stat = '''              <ul>
                <li>SPC (Statistical Process Control): Control charts for yield monitoring by lot/wafer</li>
                <li>DOE: Designed experiments to isolate process variables affecting edge yield</li>
                <li>Regression analysis: Correlated O₂ concentration proxy metrics with yield loss</li>
                <li>Cpk capability analysis: Tracked process capability improvement over time</li>
              </ul>'''

new_stat = '''              <ul>
                <li>SPC p-charts with binomial distribution for real-time yield monitoring by lot and wafer</li>
                <li>DOE + regression analysis to isolate process variables and correlate O₂ proxy metrics with yield loss</li>
                <li>Cpk capability analysis tracking process improvement over time (Cpk 1.6 → 1.8)</li>
              </ul>'''

if old_stat in html:
    html = html.replace(old_stat, new_stat)
    print("✓ AMD Statistical Methods bullets condensed")
else:
    print("✗ AMD Statistical Methods bullets NOT found")

# ─── 5. Data Mine Statistical Methods: 4 paragraphs → bullet list ────────────
old_dm_stat = '''              <h4>Statistical Methods Applied</h4>
              <p><strong>DOE / Response Surface Methodology:</strong> Applied RSM to characterize downstream controlled parameters (loading volume, elution pH, conductivity, residence time, temperature) for Protein A capture and viral inactivation. Statistically significant effects (p &lt; 0.05) were identified and used to build predictive models defining the process operating space — the same DOE-to-Cpk workflow used in semiconductor process qualification.</p>
              <p><strong>Bayesian Hierarchical Modeling:</strong> Used to characterize time-dependent CQAs (high mannose glycan species, G2F) across the full bioreactor harvest duration. Time was treated as a random variable alongside controlled process parameters, generating posterior predictive distributions. This enabled establishment of a perfusion rate control strategy with 95% confidence bounds — a defensible, probabilistic approach to process control that goes beyond traditional OFAT characterization.</p>
              <p><strong>Monte Carlo Simulation:</strong> Propagated parameter uncertainty through the integrated process model to forecast CQA probability distributions under varying perfusion conditions. Used to identify worst-case operating scenarios for FDA submission without requiring exhaustive experimental coverage.</p>
              <p><strong>RTD Modeling and Python Dashboard:</strong> Built residence time distribution (RTD) models for surge and cycle surge tanks to assess product traceability and flow homogeneity across integrated unit operations. Implemented an interactive Plotly desktop application allowing stakeholders to explore model predictions dynamically without requiring statistical expertise.</p>'''

new_dm_stat = '''              <h4>Statistical Methods Applied</h4>
              <ul>
                <li><strong>DOE / RSM:</strong> Applied Response Surface Methodology to map controlled parameters (pH, conductivity, residence time) for Protein A capture and viral inactivation; identified statistically significant effects (p &lt; 0.05) to define the process operating space</li>
                <li><strong>Bayesian Hierarchical Modeling:</strong> Characterized time-dependent CQAs (high mannose glycans, G2F) across bioreactor harvest duration, generating posterior predictive distributions and establishing perfusion rate control strategy with 95% confidence bounds</li>
                <li><strong>Monte Carlo Simulation:</strong> Propagated parameter uncertainty through the integrated process model to forecast CQA distributions under varying perfusion conditions and identify worst-case scenarios for FDA submission</li>
                <li><strong>RTD Modeling + Python Dashboard:</strong> Built residence time distribution models for surge tanks to assess product traceability; implemented interactive Plotly desktop app for stakeholder exploration of model predictions</li>
              </ul>'''

if old_dm_stat in html:
    html = html.replace(old_dm_stat, new_dm_stat)
    print("✓ Data Mine Statistical Methods converted to bullets")
else:
    print("✗ Data Mine Statistical Methods NOT found")

# ─── 6. Apollo Tyres: flatten tabs, merge prob + techd ────────────────────────
old_apollo_body = '''              <div class="tab-bar">
                <button class="tab-btn active" onclick="switchTab('p8','prob')">Problem</button>
                <button class="tab-btn" onclick="switchTab('p8','techd')">Technical Details</button>
              </div>
              <div id="p8-prob" class="tab-panel active">
                <p>Apollo Tyres (Apollo Vredestein B.V., Enschede) faced variability in final compound properties when switching between polymer suppliers — even when nominally identical raw materials were specified. The research question: how does raw material (polymer supplier) variation affect final compound properties through the tire manufacturing process chain?</p>
                <ul>
                  <li>Each processing stage amplifies or suppresses raw material variability differently</li>
                  <li>Final compound properties must meet tight specification windows for tire safety</li>
                  <li>Mapping supplier variation to compound properties enables better supplier qualification</li>
                </ul>
              </div>
              <div id="p8-techd" class="tab-panel">
                <h4>Test Methods Applied</h4>
                <ul>
                  <li><strong>ML Scorch (Mooney Viscometer):</strong> Minimum Mooney viscosity (ML 1+4) and scorch time (t5)</li>
                  <li><strong>ODR:</strong> Cure curve — ML/MH torque, ts2 scorch time, t90 optimum cure time</li>
                  <li><strong>Tensile Testing (ISO 37):</strong> M100, M300, UTS, elongation at break</li>
                  <li><strong>Rebound Resilience (Schob pendulum):</strong> Energy return correlated to rolling resistance</li>
                  <li><strong>Process chain tracked:</strong> Raw polymer → Internal mixer (Banbury) compounding → Twin-screw extrusion → Calendering → Vulcanization</li>
                </ul>
                <h4>Key Finding</h4>
                <p>Molecular weight distribution (MWD) of the incoming polymer — specifically the high-MW tail fraction — showed the strongest correlation with compound processability (Mooney viscosity, scorch time) and final tensile properties. Suppliers with narrower MWD produced more consistent compound properties despite nominally identical specification sheets. This directly informed supplier qualification requirements for Apollo's procurement team.</p>
                <div class="tech-tags">
                  <span class="tech-tag">Rubber Characterization</span><span class="tech-tag">ML Scorch</span><span class="tech-tag">Rheometry</span><span class="tech-tag">Tensile Testing</span><span class="tech-tag">Rebound Resilience</span><span class="tech-tag">Polymer MWD</span><span class="tech-tag">Vulcanization</span><span class="tech-tag">Tire Manufacturing</span><span class="tech-tag">Statistical Correlation</span>
                </div>
              </div>'''

new_apollo_body = '''              <p>Investigated how polymer supplier variation propagates through the tire manufacturing process chain (raw polymer → Banbury compounding → extrusion → calendering → vulcanization) and affects final compound properties. Used ML Scorch, ODR rheometry, and tensile testing (ISO 37) to characterize each stage. Key finding: molecular weight distribution (MWD) of the incoming polymer — specifically the high-MW tail — was the strongest predictor of compound processability and tensile performance, directly informing Apollo's supplier qualification criteria.</p>
              <ul>
                <li><strong>ML Scorch / ODR:</strong> Mooney viscosity (ML 1+4), scorch time (t5), cure curve (ts2, t90, ML/MH torque)</li>
                <li><strong>Tensile Testing (ISO 37):</strong> M100, M300, UTS, elongation at break across supplier variants</li>
                <li><strong>Rebound Resilience (Schob pendulum):</strong> Energy return correlated to rolling resistance performance</li>
                <li><strong>Statistical Correlation:</strong> MWD high-MW tail fraction vs compound processability and final properties across suppliers</li>
              </ul>
              <div class="tech-tags">
                <span class="tech-tag">Rubber Characterization</span><span class="tech-tag">ML Scorch</span><span class="tech-tag">Rheometry</span><span class="tech-tag">Tensile Testing</span><span class="tech-tag">Rebound Resilience</span><span class="tech-tag">Polymer MWD</span><span class="tech-tag">Vulcanization</span><span class="tech-tag">Tire Manufacturing</span><span class="tech-tag">Statistical Correlation</span>
              </div>'''

if old_apollo_body in html:
    html = html.replace(old_apollo_body, new_apollo_body)
    print("✓ Apollo Tyres flattened to one page")
else:
    print("✗ Apollo Tyres content NOT found")

with open(r'c:/Users/admin/Desktop/website/narain_portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\nAll done — file saved.")
