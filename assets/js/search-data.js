// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-projects",
          title: "Projects",
          description: "A collection of boring projects.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-repositories",
          title: "Repositories",
          description: "Boring repos",
          section: "Navigation",
          handler: () => {
            window.location.href = "/repositories/";
          },
        },{id: "nav-publications",
          title: "Publications",
          description: "Listed in reversed chronological order.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-news",
          title: "News",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/news/";
          },
        },{id: "nav-cv",
          title: "CV",
          description: "A short CV. You can press the button on the right to view a full one.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "dropdown-teaching",
              title: "Teaching",
              description: "",
              section: "Dropdown",
              handler: () => {
                window.location.href = "/teaching/";
              },
            },{id: "dropdown-people",
              title: "People",
              description: "",
              section: "Dropdown",
              handler: () => {
                window.location.href = "/people/";
              },
            },{id: "post-postgraduate-studies-at-sih",
        
          title: "Postgraduate studies at SIH",
        
        description: "Making right choices is crucial for your future career",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/postgraduate/";
          
        },
      },{id: "post-diet",
        
          title: "Diet",
        
        description: "Eating less and feeling more energetic",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2024/diet/";
          
        },
      },{id: "post-about-this-webpage",
        
          title: "About this webpage",
        
        description: "Why I am here",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2023/first-post/";
          
        },
      },{id: "news-recently-i-purchased-a-new-mac-mini-equipped-with-the-m2-pro-chip-for-daily-work-needs-because-my-old-macbook-pro-intel-2018-is-broken-due-to-overheat",
          title: 'Recently, I purchased a new Mac mini equipped with the M2 Pro chip...',
          description: "",
          section: "News",},{id: "news-i-am-delighted-to-share-that-the-manuscript-titled-transcription-factor-12-mediated-self-feedback-regulatory-mechanism-is-required-in-dux4-fusion-leukemia-has-been-accepted-by-the-esteemed-journal-clinical-and-translational-medicine-ctm-following-an-extensive-review-and-revision-process-spanning-nearly-two-years-i-would-like-to-express-my-sincere-gratitude-to-dr-zhihui-li-one-of-the-co-authors-for-her-invaluable-assistance-without-her-contributions-i-believe-it-would-not-have-been-possible-for-us-to-have-this-entire-story-accepted-by-ctm",
          title: 'I am delighted to share that the manuscript titled Transcription factor 12 mediated...',
          description: "",
          section: "News",},{id: "news-i-forgot-to-mention-that-hongxin-has-published-a-preview-titled-finish-the-unfinished-chd1-resolving-hexasome-nucleosome-complex-with-fact-on-19-september",
          title: 'I forgot to mention that Hongxin has published a preview titled Finish the...',
          description: "",
          section: "News",},{id: "news-molecular-mechanisms-of-unique-therapeutic-potential-of-cudc-907-for-mef2d-fusion-driven-bcp-all-has-been-published-in-signal-transduction-and-targeted-therapy",
          title: 'Molecular mechanisms of unique therapeutic potential of CUDC-907 for MEF2D fusion-driven BCP-ALL has...',
          description: "",
          section: "News",},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%66%75%72%6B%68%64%61%6E%69%73%68@%67%6D%61%69%6C.%63%6F%6D", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/danishfurekhdar", "_blank");
        },
      },{
        id: 'social-orcid',
        title: 'ORCID',
        section: 'Socials',
        handler: () => {
          window.open("https://orcid.org/0000-0003-4323-1135", "_blank");
        },
      },{
        id: 'social-researchgate',
        title: 'ResearchGate',
        section: 'Socials',
        handler: () => {
          window.open("https://www.researchgate.net/profile/Danish-Dar/", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=qOhxqbkAAAAJ", "_blank");
        },
      },{
        id: 'social-scopus',
        title: 'Scopus',
        section: 'Socials',
        handler: () => {
          window.open("https://www.scopus.com/authid/detail.uri?authorId=57219532607", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
