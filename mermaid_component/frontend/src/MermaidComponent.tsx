import {
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"
// @ts-ignore
import mermaid from 'mermaid';

const treatSource = (source: string) => {
  const index = source.indexOf("\n");
  return index === 0 ? source.substring(index + 1) : source;
}

interface State {
  html: unknown 
}

class MermaidComponent extends StreamlitComponentBase<State> {
  public state: State = { html: null }

  async componentDidMount() {
    const { args } = this.props;
    mermaid.initialize({
      startOnLoad: true,
      theme: 'default',
    });
    const source = treatSource(args["source"]);
    const html = await mermaid.render('mermaid-chart', source);
    this.setState({ html });
  }

  public render = (): ReactNode => {
    const { args } = this.props
    const { html } = this.state;

    const style: React.CSSProperties = {
      ...(args['style'] || {})
    };
    
    return html ? <div dangerouslySetInnerHTML={{ __html: html as string }} style={style} /> : null;
  }

}

export default withStreamlitConnection(MermaidComponent)
